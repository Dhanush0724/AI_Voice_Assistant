from pipeline import VoiceAssistantPipeline

if __name__ == "__main__":

    assistant = VoiceAssistantPipeline()

    # sample audio file
    input_audio = "input.wav"

    result_audio = assistant.run(input_audio)

    print("Audio response saved as:", result_audio)
