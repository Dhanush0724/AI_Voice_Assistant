import pyttsx3

class TextToSpeechService:

    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        print("TTS: Converting text to audio...")

        output_file = "output.mp3"

        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()

        return output_file
