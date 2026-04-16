# 🎤 AI Voice Assistant

An intelligent voice-based assistant that converts speech to text, processes it with AI, and responds back with synthesized speech. This project implements a complete voice interaction pipeline using modern AI technologies.

## 📋 Features

- **Speech-to-Text (STT)**: Converts audio input to text using OpenAI's Whisper model
- **Language Model (LLM)**: Generates intelligent responses using API-based LLM
- **Text-to-Speech (TTS)**: Converts responses back to natural-sounding audio
- **Modular Pipeline**: Clean architecture with separated concerns (STT, LLM, TTS)
- **Easy Integration**: Simple interface for voice interaction

## 🎧 Project Structure

```
AI_Voice_Assistant/
├── main.py              # Entry point for running the assistant
├── pipeline.py          # Main pipeline orchestrating STT → LLM → TTS
├── requirements.txt     # Python dependencies
├── services/
│   ├── stt.py          # Speech-to-Text service using Whisper
│   ├── llm.py          # Language Model service
│   └── tts.py          # Text-to-Speech service
├── input.wav           # Sample audio input
├── input2.wav          # Alternative sample audio
└── output.mp3          # Generated audio response
```

## 🚀 How It Works

The voice assistant follows a three-step pipeline:

1. **Speech-to-Text**: Audio input is transcribed to text using Whisper
2. **LLM Processing**: The text is sent to an LLM which generates an intelligent response
3. **Text-to-Speech**: The response is converted back to audio

```
[Audio Input] → [Whisper STT] → [Text] → [LLM] → [Response] → [pyttsx3 TTS] → [Audio Output]
```

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Dhanush0724/AI_Voice_Assistant.git
cd AI_Voice_Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables (if needed):
Create a `.env` file in the root directory:
```env
# Add API keys or configuration here
OPENAI_API_KEY=your_api_key_here
```

## 💻 Usage

Run the main script to process an audio file:

```bash
python main.py
```

The script will:
1. Read audio from `input.wav`
2. Transcribe the speech to text
3. Generate an AI response
4. Convert the response to audio
5. Save the output as `output.mp3`

### Example Output

```
User said: What is the weather today?
AI response: The weather information requires real-time access. Please check your local weather service.
Audio response saved as: output.mp3
```

## 🛠️ Technical Details

### Services

#### STT Service (`services/stt.py`)
- Uses OpenAI's Whisper model for accurate speech recognition
- Supports multiple audio formats (WAV, MP3, etc.)
- Returns transcribed text

#### LLM Service (`services/llm.py`)
- Integrates with language model APIs
- Generates contextual responses
- Configurable model parameters

#### TTS Service (`services/tts.py`)
- Uses pyttsx3 for text-to-speech conversion
- Generates natural-sounding audio
- Outputs MP3 format

## 🎧 Output Example

![AI Response Screenshot](Screenshot%202026-04-15%20200452.png)

*The screenshot above shows the assistant processing a voice input and generating an appropriate response.*

## 📚 Dependencies

- **whisper**: Speech-to-text transcription
- **requests**: HTTP requests for API calls
- **pyttsx3**: Text-to-speech synthesis
- **python-dotenv**: Environment variable management

See `requirements.txt` for full details.

## 🔧 Configuration

Edit `pipeline.py` to customize:
- Model parameters for STT/LLM/TTS
- API endpoints
- Audio processing settings
- Response generation behavior

## 📝 Sample Files

The repository includes sample audio files:
- `input.wav`: Example voice input for testing
- `input2.wav`: Alternative example
- `output.mp3`: Generated response example

## 🐛 Troubleshooting

**Issue**: Audio file not found
- **Solution**: Ensure audio file is in the correct path or update the filename in `main.py`

**Issue**: API key errors
- **Solution**: Verify your API keys are correctly set in the `.env` file

**Issue**: Whisper model not loading
- **Solution**: Ensure whisper is properly installed: `pip install --upgrade openai-whisper`

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

For questions or support, please open an issue on the GitHub repository.

---

**Built with ❤️ for AI-powered voice interactions**