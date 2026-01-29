import os
import requests
from dotenv import load_dotenv

class LLMService:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY")

        self.url = "https://openrouter.ai/api/v1/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_response(self, user_text):
        print("LLM: Sending prompt to OpenRouter...")

        data = {
            "model": "mistralai/mixtral-8x7b-instruct",  
            "messages": [
                {"role": "user", "content": user_text}
            ],
            "max_tokens": 50
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        result = response.json()

        ai_text = result["choices"][0]["message"]["content"]

        return ai_text
