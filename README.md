# 🎤 Hindi-Speaking AI Assistant

A full-stack Hindi-speaking AI assistant with speech-to-text, intelligent response generation, and text-to-speech capabilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Features

### Core Capabilities
- **🎙️ Speech-to-Text (Hindi)**: Convert Hindi speech to text using Google Gemini 2.0 Flash
- **🤖 AI Response Generation**: Generate intelligent Hindi responses using Gemini LLM
- **🔊 Text-to-Speech (Hindi)**: Convert Hindi text to natural speech using Google TTS
- **📁 File Upload**: Process pre-recorded Hindi audio files (MP3, WAV, M4A, OGG, WEBM)
- **🎯 Live Recording**: Record and process speech in real-time using browser's Web Speech API

### Technical Features
- Clean REST API with FastAPI
- Real-time audio processing
- Rate limiting for API calls
- Modern, responsive UI
- CORS-enabled for cross-origin requests
- Async/await architecture

## 🏗️ Project Structure

```
AIdemos/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── config.py              # Configuration management
│   ├── requirements.txt       # Python dependencies
│   ├── routes/
│   │   ├── audio.py          # Audio processing endpoints
│   │   └── system.py         # Health check endpoints
│   ├── services/
│   │   ├── gemini_service.py # Gemini API integration
│   │   └── tts_service.py    # Text-to-speech service
│   ├── uploads/              # Uploaded audio files
│   └── outputs/              # Generated audio responses
├── frontend/
│   └── index.html            # Web interface
├── setup.ps1                 # Setup script (PowerShell)
├── setup.bat                 # Setup script (Batch)
└── README.md                 # Documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download the repository**

```bash
cd AIdemos
```

2. **Run the automated setup script**

**For PowerShell:**
```powershell
.\setup.ps1
```

**For Command Prompt:**
```batch
setup.bat
```

3. **Configure API Key**

The setup script will create a `.env` file. Edit it and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### Manual Setup (Alternative)

If you prefer manual setup:

1. **Create virtual environment**
```bash
python -m venv venv
```

2. **Activate virtual environment**
```powershell
# PowerShell
.\venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate.bat
```

3. **Install dependencies**
```bash
pip install -r backend\requirements.txt
```

4. **Create .env file**
```bash
copy backend\.env.example backend\.env
```
Then edit `backend\.env` and add your API key.

## 🎯 Usage

### Starting the Application

#### Option 1: Using Start Scripts

**Backend (Terminal 1):**
```powershell
cd backend
.\start_backend.ps1  # PowerShell
# OR
start_backend.bat    # Command Prompt
```

**Frontend (Terminal 2):**
```powershell
cd frontend
.\start_frontend.ps1  # PowerShell
# OR
start_frontend.bat    # Command Prompt
```

#### Option 2: Manual Start

**Backend:**
```bash
cd backend
python app.py
```
Backend will run on: http://localhost:8000

**Frontend:**
```bash
cd frontend
python run_frontend.py
```
Frontend will run on: http://localhost:3000

### Using the Application

1. **Open the frontend** in your browser: http://localhost:3000

2. **Choose one of two options:**

   **Option A: Live Speech Recognition**
   - Click "🎙️ Start Listening"
   - Speak in Hindi
   - Click "Stop Listening" when done
   - Your speech will be processed automatically

   **Option B: Upload Audio File**
   - Click "📁 Choose Hindi Audio File"
   - Select a Hindi audio file (MP3, WAV, M4A, OGG, WEBM)
   - Click "🎵 Process Audio"

3. **View Results:**
   - **Transcription**: Your Hindi speech converted to text
   - **AI Response**: Intelligent Hindi response from Gemini
   - **Audio Response**: Listen to the AI's response

## 🔧 API Endpoints

### System Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation (Swagger UI)

### Audio Processing Endpoints

- `POST /api/process-audio` - Process uploaded audio file
- `POST /api/process-text` - Process text directly (from live recording)
- `GET /api/audio/{filename}` - Get generated audio file
- `DELETE /api/cleanup` - Clean up temporary files

### Example API Usage

```python
import requests

# Process audio file
files = {'audio_file': open('hindi_audio.mp3', 'rb')}
response = requests.post('http://localhost:8000/api/process-audio', files=files)
data = response.json()

print(f"Transcription: {data['transcription']}")
print(f"Response: {data['response']}")
print(f"Audio URL: {data['audio_url']}")
```

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Google Gemini 2.5 Flash**: Speech-to-text and response generation
- **gTTS (Google Text-to-Speech)**: Hindi text-to-speech conversion
- **Python 3.8+**: Programming language
- **Uvicorn**: ASGI server

### Frontend
- **HTML5**: Web structure
- **CSS3**: Styling with gradients and animations
- **Vanilla JavaScript**: Client-side logic
- **Web Speech API**: Live speech recognition (browser-based)
- **MediaRecorder API**: Audio recording

## 📊 Configuration

All configuration is managed through environment variables in `backend/.env`:

```env
# API Keys
GEMINI_API_KEY=your_gemini_api_key_here

# Server Settings
HOST=0.0.0.0
PORT=8000
RELOAD=True

# CORS Settings
CORS_ORIGINS=*

# Logging
LOG_LEVEL=INFO
```

## 🔒 Security Notes

- Never commit your `.env` file or expose your API keys
- Use environment variables for sensitive data
- Implement rate limiting in production
- Validate and sanitize all user inputs
- Use HTTPS in production environments

## 🐛 Troubleshooting

### Common Issues

**1. "GEMINI_API_KEY not configured"**
- Solution: Add your API key to `backend/.env`

**2. "Rate limit exceeded"**
- Solution: Wait 2-3 minutes between requests or upgrade your Gemini API plan

**3. "Module not found" errors**
- Solution: Ensure virtual environment is activated and run `pip install -r backend/requirements.txt`

**4. "Microphone access denied"**
- Solution: Grant microphone permissions in your browser settings

**5. CORS errors**
- Solution: Ensure both backend and frontend are running on correct ports

## 📝 Development

### Running in Development Mode

```bash
# Backend with auto-reload
cd backend
uvicorn app:app --reload --port 8000

# Frontend
cd frontend
python run_frontend.py
```

### Testing the API

Use the interactive documentation at http://localhost:8000/docs to test endpoints.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.


## 🙏 Acknowledgments

- Google Gemini AI for speech-to-text and response generation
- Google Text-to-Speech (gTTS) for audio synthesis
- FastAPI for the excellent web framework
- The open-source community

## 📧 Support

For issues, questions, or suggestions, please open an issue in the repository.

---
