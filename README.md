# Voice Enabled AI Assistant

This project implements a simple voice-enabled AI assistant that follows a complete pipeline:

Voice Input → Speech to Text → LLM Response → Text to Speech → Audio Output

The goal of this project is to demonstrate system design, clean architecture, and understanding of voice AI workflows.

---

## 🔧 Project Structure

voice_ai_assistant/

├── main.py  
├── pipeline.py  
├── services/  
│   ├── stt.py  
│   ├── llm.py  
│   ├── tts.py  
├── .env.example  
├── requirements.txt  
└── README.md  

---

## ⚙️ Features

- Modular pipeline design
- Speech to Text (mock implementation)
- LLM response using OpenRouter API
- Text to Speech audio generation
- Easy to extend with real APIs or models

---

## 🚀 How It Works

1. User provides voice input (audio file or simulated)
2. STT converts audio into text (mocked)
3. Text is sent to an LLM via OpenRouter
4. LLM generates a response
5. Response is converted to speech audio

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Dhanush0724/AI_Voice_Assistant.git
cd AI_Voice_Assistant
2. Install dependencies
pip install -r requirements.txt
```
### 3. Setup environment variables

Create a .env file in project root:

OPENROUTER_API_KEY=your_api_key_here


(Refer to .env.example)

### 4. Run the project
```bash
python main.py
```

### 🎧 Output

After running:

Console will display the pipeline flow

An audio file output.mp3 will be generated with AI response voice
