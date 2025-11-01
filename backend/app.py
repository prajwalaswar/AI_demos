"""
Hindi-Speaking AI Assistant - Main Application
FastAPI backend for Hindi speech-to-text, response generation, and text-to-speech
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, CORS_ORIGINS
from routes import system, audio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI application
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(system.router)
app.include_router(audio.router)


@app.on_event("startup")
async def startup_event():
    """Execute on application startup"""
    logger.info(f"🚀 Starting {APP_TITLE} v{APP_VERSION}")
    logger.info(f"📚 API Documentation: http://localhost:8000/docs")


@app.on_event("shutdown")
async def shutdown_event():
    """Execute on application shutdown"""
    logger.info("🛑 Shutting down application")


if __name__ == "__main__":
    import uvicorn
    from config import HOST, PORT, RELOAD
    
    logger.info(f"Starting server on {HOST}:{PORT}")
    uvicorn.run(
        "app:app",
        host=HOST,
        port=PORT,
        reload=RELOAD,
        log_level="info"
    )

