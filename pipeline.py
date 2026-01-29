from services.stt import SpeechToTextService
from services.llm import LLMService
from services.tts import TextToSpeechService

class VoiceAssistantPipeline:

    def __init__(self):
        self.stt_service = SpeechToTextService()
        self.llm_service = LLMService()
        self.tts_service = TextToSpeechService()

    def run(self, audio_file):

        # Step 1: Speech to Text
        text = self.stt_service.transcribe(audio_file)
        print("User said:", text)

        # Step 2: LLM Response
        response = self.llm_service.generate_response(text)
        print("AI response:", response)

        # Step 3: Text to Speech
        audio_output = self.tts_service.speak(response)

        return audio_output
