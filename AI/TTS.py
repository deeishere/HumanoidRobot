from elevenlabs.client import ElevenLabs
from elevenlabs import play

class TTSService:
    def __init__(self, api_key='sk_5aafdd7c5759c36262c5f5381f5d6b8228a69d22fa538b7e'):
        self.client = ElevenLabs(api_key=api_key)
    
    def speak(self, text, voice="Bill", model="eleven_multilingual_v2"):
        """
        Convert text to speech and play it
        
        Args:
            text: The text to convert to speech
            voice: Voice ID or name to use
            model: ElevenLabs model to use
        """
        audio = self.client.generate(
            text=text,
            voice=voice,
            model=model
        )
        play(audio)

# For direct testing
if __name__ == "__main__":
    tts = TTSService()
    tts.speak("السلام عليكم, أنا من نادي الدرونز و الروبوت")
