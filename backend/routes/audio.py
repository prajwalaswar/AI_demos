"""
Audio Processing API Endpoints
Handles audio upload, transcription, response generation, and TTS
"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import logging
from pathlib import Path

from services.gemini_service import GeminiService
from services.tts_service import TTSService
from config import UPLOAD_DIR, OUTPUT_DIR, ALLOWED_AUDIO_EXTENSIONS, GEMINI_API_KEY

logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="/api", tags=["audio"])

# Initialize services (singleton pattern)
gemini_service = GeminiService(api_key=GEMINI_API_KEY)
tts_service = TTSService()


# Pydantic model for text processing
class TextRequest(BaseModel):
    text: str


@router.post("/process-audio")
async def process_audio(audio_file: UploadFile = File(...)):
    """
    Process uploaded audio files (for file upload functionality)
    
    Steps:
    1. Receive audio file (MP3/WAV/M4A/OGG/WEBM/WEBA)
    2. Use Gemini to transcribe Hindi speech to text
    3. Generate Hindi response using Gemini LLM
    4. Convert response to speech using gTTS
    5. Return transcription, response text, and audio file
    
    Note: For live recording, use /process-text endpoint with Web Speech API
    
    Args:
        audio_file: Uploaded audio file
        
    Returns:
        JSON with transcription, response, and audio URL
    """
    try:
        logger.info(f"Received audio file: {audio_file.filename}")
        
        # Validate file type
        file_ext = Path(audio_file.filename).suffix.lower()
        if file_ext not in ALLOWED_AUDIO_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid file format. Allowed formats: {', '.join(ALLOWED_AUDIO_EXTENSIONS)}"
            )
        
        # Save uploaded audio file
        audio_path = UPLOAD_DIR / audio_file.filename
        with open(audio_path, "wb") as f:
            content = await audio_file.read()
            f.write(content)
        
        logger.info(f"Audio file saved to: {audio_path}")
        
        # Step 1: Transcribe Hindi speech to text using Gemini
        logger.info("Transcribing audio with Gemini...")
        transcription = await gemini_service.transcribe_audio(str(audio_path))
        
        if not transcription:
            raise HTTPException(
                status_code=429,
                detail="Failed to transcribe audio. If you're getting rate limited, please wait 2-3 minutes and try again. Otherwise, ensure the audio is clear and in Hindi."
            )
        
        logger.info(f"Transcription: {transcription}")
        
        # Step 2: Generate Hindi response using Gemini LLM
        logger.info("Generating response with Gemini LLM...")
        response_text = await gemini_service.generate_response(transcription)
        
        if not response_text:
            raise HTTPException(
                status_code=500,
                detail="Failed to generate response"
            )
        
        logger.info(f"Response: {response_text}")
        
        # Step 3: Convert response to speech using gTTS
        logger.info("Converting response to speech...")
        audio_filename = f"response_{Path(audio_file.filename).stem}.mp3"
        audio_output_path = OUTPUT_DIR / audio_filename
        
        success = await tts_service.text_to_speech(response_text, str(audio_output_path))
        
        if not success:
            raise HTTPException(
                status_code=500,
                detail="Failed to generate speech audio"
            )
        
        logger.info(f"Audio response saved to: {audio_output_path}")
        
        # Return response with audio file URL
        return JSONResponse(content={
            "success": True,
            "transcription": transcription,
            "response": response_text,
            "audio_url": f"/api/audio/{audio_filename}"
        })
        
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error processing audio: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@router.get("/audio/{filename}")
async def get_audio(filename: str):
    """
    Serve generated audio files
    
    Args:
        filename: Name of the audio file
        
    Returns:
        Audio file response
    """
    audio_path = OUTPUT_DIR / filename
    
    if not audio_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Audio file not found"
        )
    
    return FileResponse(
        path=audio_path,
        media_type="audio/mpeg",
        filename=filename
    )


@router.post("/process-text")
async def process_text(request: TextRequest):
    """
    Process text directly (from Web Speech API)
    
    Steps:
    1. Receive transcribed text from frontend
    2. Generate Hindi response using Gemini LLM
    3. Convert response to speech using gTTS
    4. Return response text and audio file
    
    Args:
        request: TextRequest with transcribed text
        
    Returns:
        JSON with transcription, response, and audio URL
    """
    try:
        logger.info(f"Received text for processing: {request.text}")
        
        # Step 1: Generate Hindi response using Gemini LLM
        logger.info("Generating response with Gemini LLM...")
        response_text = await gemini_service.generate_response(request.text)
        
        if not response_text:
            raise HTTPException(
                status_code=500,
                detail="Failed to generate response"
            )
        
        logger.info(f"Response: {response_text}")
        
        # Step 2: Convert response to speech using gTTS
        logger.info("Converting response to speech...")
        import uuid
        unique_id = str(uuid.uuid4())
        audio_filename = f"response_text_{unique_id}.mp3"
        audio_output_path = OUTPUT_DIR / audio_filename
        
        success = await tts_service.text_to_speech(response_text, str(audio_output_path))
        
        if not success:
            raise HTTPException(
                status_code=500,
                detail="Failed to generate speech audio"
            )
        
        logger.info(f"Audio response saved to: {audio_output_path}")
        
        # Return results
        return {
            "transcription": request.text,  # Return the original text
            "response": response_text,
            "audio_url": f"/api/audio/{audio_filename}"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing text: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process text: {str(e)}"
        )


@router.delete("/cleanup")
async def cleanup_files():
    """
    Clean up uploaded and generated files
    
    Returns:
        Success message
    """
    try:
        # Clean uploads
        upload_count = 0
        for file in UPLOAD_DIR.glob("*"):
            if file.is_file():
                file.unlink()
                upload_count += 1
        
        # Clean outputs
        output_count = 0
        for file in OUTPUT_DIR.glob("*"):
            if file.is_file():
                file.unlink()
                output_count += 1
        
        logger.info(f"Cleaned {upload_count} uploads and {output_count} outputs")
        
        return {
            "message": "Files cleaned up successfully",
            "uploads_deleted": upload_count,
            "outputs_deleted": output_count
        }
    except Exception as e:
        logger.error(f"Cleanup failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Cleanup failed: {str(e)}"
        )
