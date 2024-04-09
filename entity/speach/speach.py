import requests
import json
import config

url = 'http://api.elevenlabs.io/v1/voices'

headers = {
    "Accept": "application/json",
    "xi-api-key": config.ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}


class Speach:
    def __init__(self, text):
        self.text = text

    def get_voices(self):
        response = requests.get(url, headers=headers)
        data = response.json()

        for voice in data['voices']:
            print(f"{voice['name']}; {voice['voice_id']}")

    def text_to_speach(self):
        CHUNK_SIZE = 1024
        XI_API_KEY = config.ELEVENLABS_API_KEY
        VOICE_ID = "pNInz6obpgDQGcFmaJgB"
        TEXT_TO_SPEAK = self.text
        OUTPUT_PATH = "output.mp3"

        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

        headers = {
            "Accept": "application/json",
            "xi-api-key": XI_API_KEY
        }

        data = {
            "text": TEXT_TO_SPEAK,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }

        response = requests.post(tts_url, headers=headers, json=data, stream=True)

        if response.ok:
            with open(OUTPUT_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)
            print("Audio stream saved successfully.")
        else:
            print(response.text)
