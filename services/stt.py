import whisper

class SpeechToTextService:

    def __init__(self):
        
        self.model = whisper.load_model("base")
        print("STT: Whisper model loaded successfully")

    def transcribe(self, audio_path):
      
        print(f"STT: Transcribing audio file: {audio_path}")
        
        try:
          
            result = self.model.transcribe(audio_path)
            text = result["text"].strip()
            
            print(f"STT: Successfully transcribed: {text}")
            return text
                
        except Exception as e:
            print(f"STT: Error during transcription: {e}")
            return ""