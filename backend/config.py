"""
Configuration Management for Hindi AI Assistant
Centralized configuration with environment variables
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
    raise ValueError(
        "GEMINI_API_KEY not configured. "
        "Please add your API key to the .env file. "
        "Get one at: https://makersuite.google.com/app/apikey"
    )

# Server Configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
RELOAD = os.getenv("RELOAD", "True").lower() == "true"

# CORS Configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

# Directory Configuration
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

# Create directories if they don't exist
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# File Upload Configuration
MAX_UPLOAD_SIZE = 25 * 1024 * 1024  # 25MB
ALLOWED_AUDIO_EXTENSIONS = ['.mp3', '.wav', '.m4a', '.ogg', '.webm', '.weba']

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Application Metadata
APP_TITLE = "Hindi-Speaking AI Assistant"
APP_DESCRIPTION = "AI Assistant with Hindi Speech-to-Text, LLM Response, and Text-to-Speech"
APP_VERSION = "1.0.0"
