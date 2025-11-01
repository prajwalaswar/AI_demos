"""
Frontend Server Startup Script
Serves the Hindi AI Assistant frontend using Python's built-in HTTP server
"""

import http.server
import socketserver
import webbrowser
import logging
import os
from pathlib import Path

# Configuration
PORT = 3000
HOST = "localhost"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom log format"""
        logger.info(f"{self.address_string()} - {format % args}")


def main():
    """Start the frontend HTTP server"""
    # Change to frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    logger.info("=" * 70)
    logger.info("🎨 Hindi AI Assistant - Frontend Server")
    logger.info("=" * 70)
    logger.info(f"📁 Serving from: {frontend_dir}")
    logger.info(f"🌐 Frontend URL: http://{HOST}:{PORT}")
    logger.info(f"📄 Main page: http://{HOST}:{PORT}/index.html")
    logger.info("=" * 70)
    logger.info("⚠️  Make sure the backend server is running on port 8000")
    logger.info("=" * 70)
    logger.info("Press CTRL+C to stop the server")
    logger.info("=" * 70)
    
    # Create server
    Handler = CustomHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            # Open browser automatically
            url = f"http://{HOST}:{PORT}/index.html"
            logger.info(f"\n🚀 Opening browser at {url}...\n")
            webbrowser.open(url)
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        logger.info("\n" + "=" * 70)
        logger.info("🛑 Frontend server stopped by user")
        logger.info("=" * 70)
    except OSError as e:
        if "Address already in use" in str(e):
            logger.error(f"\n❌ Port {PORT} is already in use!")
            logger.error("Please close the other application or change the PORT in this script")
        else:
            logger.error(f"\n❌ Error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"\n❌ Unexpected error: {str(e)}")
        raise


if __name__ == "__main__":
    main()
