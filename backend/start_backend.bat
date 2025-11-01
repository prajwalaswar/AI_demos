@echo off
REM Backend Server Startup Script for Windows
REM Starts the Hindi AI Assistant backend server

echo ========================================
echo   Hindi AI Assistant - Backend Server
echo ========================================
echo.

REM Check if we're in the backend directory
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please run this script from the backend directory
    pause
    exit /b 1
)

REM Check if virtual environment is activated
python -c "import sys; sys.exit(0 if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) else 1)"
if errorlevel 1 (
    echo WARNING: Virtual environment not activated!
    echo Attempting to activate...
    if exist "..\venv\Scripts\activate.bat" (
        call ..\venv\Scripts\activate.bat
    ) else (
        echo ERROR: Virtual environment not found!
        echo Please run setup.bat first
        pause
        exit /b 1
    )
)

echo.
echo Starting backend server...
echo.
echo Server will start on http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.

REM Start the server
python run_backend.py

echo.
echo ========================================
echo Server stopped
echo ========================================
pause
