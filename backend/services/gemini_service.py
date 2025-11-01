"""
Gemini Service - Speech-to-Text and Response Generation
Uses Google Gemini 2.5 Flash for Hindi language processing
"""

import google.generativeai as genai
import logging
from typing import Optional
import asyncio
from pathlib import Path
import time

logger = logging.getLogger(__name__)


class GeminiService:
    """Service for Gemini API interactions"""
    
    def __init__(self, api_key: str):
        """Initialize Gemini service with API key"""
        self.api_key = api_key
        genai.configure(api_key=api_key)
        
        # Initialize model
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Rate limiting
        self.last_request_time = 0
        self.min_request_interval = 2  # seconds between requests
        
        logger.info("Gemini Service initialized")
    
    async def transcribe_audio(self, audio_path: str) -> Optional[str]:
        """
        Transcribe Hindi audio to text
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Transcribed Hindi text or None if failed
        """
        try:
            # Rate limiting
            await self._rate_limit()
            
            # Read audio file
            audio_file = Path(audio_path)
            if not audio_file.exists():
                logger.error(f"Audio file not found: {audio_path}")
                return None
            
            with open(audio_path, 'rb') as f:
                audio_data = f.read()
            
            # Transcription prompt
            prompt = "Transcribe this Hindi audio accurately. Return ONLY the Devanagari text without explanations."
            
            # Generate transcription
            content_parts = [
                prompt,
                {"mime_type": "audio/webm", "data": audio_data}
            ]
            
            response = await asyncio.to_thread(
                self.model.generate_content,
                content_parts
            )
            
            transcription = response.text.strip()
            logger.info(f"Transcription: {transcription[:50]}...")
            
            return transcription
            
        except Exception as e:
            logger.error(f"Transcription error: {str(e)}")
            return None
    
    async def generate_response(self, user_input: str) -> Optional[str]:
        """
        Generate Hindi response using Gemini LLM
        
        Args:
            user_input: Hindi text from user
            
        Returns:
            Generated Hindi response or None if failed
        """
        try:
            # Rate limiting
            await self._rate_limit()
            
            # Response generation prompt
            prompt = f"""You are a helpful Hindi-speaking AI assistant.
Respond ONLY in Hindi (Devanagari script).
Keep responses concise (2-3 sentences).
Be polite and helpful.

User said: {user_input}

Response:"""
            
            # Generate response
            response = await asyncio.to_thread(
                self.model.generate_content,
                prompt
            )
            
            hindi_response = response.text.strip()
            logger.info(f"Response generated: {hindi_response[:50]}...")
            
            return hindi_response
            
        except Exception as e:
            logger.error(f"Response generation error: {str(e)}")
            return None
    
    async def _rate_limit(self):
        """Apply rate limiting between API calls"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.min_request_interval:
            wait_time = self.min_request_interval - time_since_last
            await asyncio.sleep(wait_time)
        
        self.last_request_time = time.time()
