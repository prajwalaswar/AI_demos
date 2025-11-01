"""
Text-to-Speech Service using Google TTS
Converts Hindi text to speech audio
"""

from gtts import gTTS
import logging
import asyncio
from pathlib import Path

logger = logging.getLogger(__name__)


class TTSService:
    """Service for Text-to-Speech conversion"""
    
    def __init__(self):
        """Initialize TTS service"""
        logger.info("TTS Service initialized")
    
    async def text_to_speech(self, text: str, output_path: str, language: str = 'hi') -> bool:
        """
        Convert Hindi text to speech audio
        
        Args:
            text: Hindi text to convert
            output_path: Path to save audio file
            language: Language code (default: 'hi' for Hindi)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not text or not text.strip():
                logger.error("Empty text provided")
                return False
            
            # Create TTS object
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Save audio file
            await asyncio.to_thread(tts.save, output_path)
            
            # Verify file creation
            if Path(output_path).exists():
                logger.info(f"Audio saved: {output_path}")
                return True
            else:
                logger.error("Failed to save audio file")
                return False
                
        except Exception as e:
            logger.error(f"TTS error: {str(e)}")
            return False
