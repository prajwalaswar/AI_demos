"""
System Health Check API Endpoints
"""

from fastapi import APIRouter
from config import APP_TITLE, APP_VERSION

# Create router
router = APIRouter(tags=["system"])


@router.get("/")
async def root():
    """
    Root endpoint - API information
    """
    return {
        "message": APP_TITLE,
        "version": APP_VERSION,
        "status": "active",
        "endpoints": {
            "/": "API information",
            "/health": "Health check",
            "/api/process-audio": "Process audio file",
            "/api/process-text": "Process text directly",
            "/api/audio/{filename}": "Get audio file",
            "/api/cleanup": "Clean temporary files",
            "/docs": "API documentation"
        }
    }


@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "version": APP_VERSION
    }
