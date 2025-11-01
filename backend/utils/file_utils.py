"""
Utility functions for audio processing and file handling
"""

import os
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def validate_audio_file(file_path: str) -> bool:
    """
    Validate if file exists and is a valid audio file
    
    Args:
        file_path: Path to audio file
        
    Returns:
        True if valid, False otherwise
    """
    try:
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            logger.error(f"File does not exist: {file_path}")
            return False
        
        # Check if it's a file (not directory)
        if not path.is_file():
            logger.error(f"Path is not a file: {file_path}")
            return False
        
        # Check file extension
        valid_extensions = ['.mp3', '.wav', '.m4a', '.ogg', '.webm']
        if path.suffix.lower() not in valid_extensions:
            logger.error(f"Invalid audio file extension: {path.suffix}")
            return False
        
        # Check file size (max 25MB)
        max_size = 25 * 1024 * 1024  # 25MB in bytes
        if path.stat().st_size > max_size:
            logger.error(f"File too large: {path.stat().st_size} bytes")
            return False
        
        return True
        
    except Exception as e:
        logger.error(f"Error validating audio file: {str(e)}")
        return False


def cleanup_old_files(directory: str, max_age_hours: int = 24):
    """
    Clean up old files from a directory
    
    Args:
        directory: Directory path to clean
        max_age_hours: Maximum age of files in hours
    """
    try:
        import time
        
        dir_path = Path(directory)
        if not dir_path.exists():
            return
        
        current_time = time.time()
        max_age_seconds = max_age_hours * 3600
        
        for file_path in dir_path.glob("*"):
            if file_path.is_file():
                file_age = current_time - file_path.stat().st_mtime
                if file_age > max_age_seconds:
                    file_path.unlink()
                    logger.info(f"Deleted old file: {file_path}")
                    
    except Exception as e:
        logger.error(f"Error cleaning up files: {str(e)}")


def ensure_directories_exist():
    """Create necessary directories if they don't exist"""
    directories = ['uploads', 'outputs', 'temp']
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        logger.info(f"Directory ensured: {directory}")


def get_file_size_mb(file_path: str) -> float:
    """
    Get file size in megabytes
    
    Args:
        file_path: Path to file
        
    Returns:
        File size in MB
    """
    try:
        size_bytes = Path(file_path).stat().st_size
        size_mb = size_bytes / (1024 * 1024)
        return round(size_mb, 2)
    except Exception as e:
        logger.error(f"Error getting file size: {str(e)}")
        return 0.0
