# Hindi AI Assistant - Windows Setup Script
# Run this script to automatically set up the project

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Hindi-Speaking AI Assistant - Setup Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Check if venv exists
Write-Host ""
Write-Host "Checking virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "✗ Virtual environment not found" -ForegroundColor Red
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
Set-Location backend
pip install -r requirements.txt --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ All dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Error installing dependencies" -ForegroundColor Red
    exit 1
}

# Check .env file
Write-Host ""
Write-Host "Checking configuration..." -ForegroundColor Yellow
if (Test-Path ".env") {
    $envContent = Get-Content ".env" -Raw
    if ($envContent -match "your_gemini_api_key_here") {
        Write-Host "⚠ WARNING: Please add your Gemini API key in backend\.env" -ForegroundColor Yellow
        Write-Host "  Get your key from: https://makersuite.google.com/app/apikey" -ForegroundColor Cyan
    } else {
        Write-Host "✓ Configuration file found and appears configured" -ForegroundColor Green
    }
} else {
    Write-Host "✗ .env file not found!" -ForegroundColor Red
}

# Create directories if they don't exist
Write-Host ""
Write-Host "Setting up directories..." -ForegroundColor Yellow
@("uploads", "outputs") | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Path $_ | Out-Null
    }
}
Write-Host "✓ Directories ready" -ForegroundColor Green

# Display next steps
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Setup Complete! Next Steps:" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Add your Gemini API key to backend\.env" -ForegroundColor Yellow
Write-Host "   Get key: https://makersuite.google.com/app/apikey" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Start the server:" -ForegroundColor Yellow
Write-Host "   cd backend" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor White
Write-Host ""
Write-Host "3. Open frontend in browser:" -ForegroundColor Yellow
Write-Host "   Open frontend\index.html in your browser" -ForegroundColor White
Write-Host ""
Write-Host "4. Test the API (optional):" -ForegroundColor Yellow
Write-Host "   python test_api.py" -ForegroundColor White
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "For detailed instructions, see QUICKSTART.md" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
