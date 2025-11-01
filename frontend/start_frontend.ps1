# Frontend Server Startup Script for Windows PowerShell
# Serves the Hindi AI Assistant frontend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Hindi AI Assistant - Frontend Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the frontend directory
if (-not (Test-Path "index.html")) {
    Write-Host "ERROR: index.html not found!" -ForegroundColor Red
    Write-Host "Please run this script from the frontend directory" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Starting frontend server..." -ForegroundColor Green
Write-Host ""
Write-Host "Frontend URL: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Main page: http://localhost:3000/index.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "Make sure the backend server is running on port 8000!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Start Python HTTP server
try {
    python run_frontend.py
} catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start server" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Server stopped" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
