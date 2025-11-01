# Backend Server Startup Script for Windows PowerShell
# Starts the Hindi AI Assistant backend server

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Hindi AI Assistant - Backend Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the backend directory
if (-not (Test-Path "app.py")) {
    Write-Host "ERROR: app.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the backend directory" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if virtual environment is activated
$venvActive = $env:VIRTUAL_ENV
if (-not $venvActive) {
    Write-Host "WARNING: Virtual environment not activated!" -ForegroundColor Yellow
    Write-Host "Attempting to activate..." -ForegroundColor Yellow
    if (Test-Path "..\venv\Scripts\Activate.ps1") {
        & "..\venv\Scripts\Activate.ps1"
    } else {
        Write-Host "ERROR: Virtual environment not found!" -ForegroundColor Red
        Write-Host "Please run setup.ps1 first" -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "Starting backend server..." -ForegroundColor Green
Write-Host ""
Write-Host "Server will start on http://localhost:8000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start the server
try {
    python run_backend.py
} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start server" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Server stopped" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
