"""
Backend Server Startup Script
Run this file to start the Hindi AI Assistant backend server
"""

import uvicorn
import logging
from config import HOST, PORT, RELOAD, APP_TITLE, APP_VERSION

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Start the FastAPI backend server"""
    logger.info("=" * 70)
    logger.info(f"🚀 {APP_TITLE} - Backend Server")
    logger.info(f"📦 Version: {APP_VERSION}")
    logger.info("=" * 70)
    logger.info(f"🌐 Starting server on http://{HOST}:{PORT}")
    logger.info(f"📚 API Documentation: http://{HOST}:{PORT}/docs")
    logger.info(f"📖 Alternative Docs: http://{HOST}:{PORT}/redoc")
    logger.info("=" * 70)
    logger.info("Press CTRL+C to stop the server")
    logger.info("=" * 70)
    
    try:
        uvicorn.run(
            "app:app",
            host=HOST,
            port=PORT,
            reload=RELOAD,
            log_level="info"
        )
    except KeyboardInterrupt:
        logger.info("\n" + "=" * 70)
        logger.info("🛑 Server stopped by user")
        logger.info("=" * 70)
    except Exception as e:
        logger.error(f"❌ Error starting server: {str(e)}")
        raise


if __name__ == "__main__":
    main()
