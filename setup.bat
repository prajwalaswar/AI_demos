@echo off
echo ================================================
echo   Hindi-Speaking AI Assistant - Quick Setup
echo ================================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found! Please install Python 3.8+
    pause
    exit /b 1
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
cd backend
pip install -r requirements.txt

echo.
echo ================================================
echo   Setup Complete!
echo ================================================
echo.
echo NEXT STEPS:
echo 1. Add your Gemini API key in backend\.env
echo 2. Run: python app.py
echo 3. Open frontend\index.html in browser
echo.
echo See QUICKSTART.md for detailed instructions
echo ================================================
pause
