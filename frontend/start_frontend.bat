@echo off
REM Frontend Server Startup Script for Windows
REM Serves the Hindi AI Assistant frontend

echo ========================================
echo   Hindi AI Assistant - Frontend Server
echo ========================================
echo.

REM Check if we're in the frontend directory
if not exist "index.html" (
    echo ERROR: index.html not found!
    echo Please run this script from the frontend directory
    pause
    exit /b 1
)

echo Starting frontend server...
echo.
echo Frontend URL: http://localhost:3000
echo Main page: http://localhost:3000/index.html
echo.
echo Make sure the backend server is running on port 8000!
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.

REM Start Python HTTP server
python run_frontend.py

echo.
echo ========================================
echo Server stopped
echo ========================================
pause
