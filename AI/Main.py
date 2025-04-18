import asyncio
import time
import os
import threading
import signal
import sys

#Import from Chat, TTS, STT Classes
from STT import transcribe_audio
from TTS import TTSService
from Chat import DeepSeekChat, DEEPSEEK_API_KEY

class AsyncVoiceAssistant:
    def __init__(self):
        # Initialize components
        self.tts_service = TTSService()
        self.deepseek = DeepSeekChat(DEEPSEEK_API_KEY)
        self.is_listening = True
        self.is_processing = False
        self.should_exit = False
        
        # Initialize conversation history with system prompt
        self.conversation_history = [
            {"role": "system", "content": "You are a bilingual helpful assistant for a drone and robotics club. You speak arabic and english. Always respond in short and concise manner. Reply in english when asked in english and in arabic when asked in arabic."}
        ]
        
        # Set up signal handling for graceful exit
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C and other termination signals"""
        print("\nShutting down assistant gracefully...")
        self.should_exit = True
        self.is_listening = False
        time.sleep(1)  # Give threads time to clean up
        sys.exit(0)
    
    async def process_voice(self, user_input):
        """Process transcribed voice input and generate response"""
        self.is_processing = True
        
        # Check for exit command
        if any(exit_word in user_input.lower() for exit_word in ["exit", "quit", "bye", "goodbye"]):
            print("Exit command detected.")
            await self.speak("Goodbye!")
            self.should_exit = True
            self.is_processing = False
            return
        
        # Check for clear history command
        if "clear history" in user_input.lower() or "reset conversation" in user_input.lower():
            self.clear_history()
            response = "Conversation history cleared. What would you like to talk about?"
            print(response)
            await self.speak(response)
            self.is_processing = False
            return
        
        # Add user message to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        print("Processing...")
        
        # Use the Chat module to get a response (run in thread pool to avoid blocking)
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, 
            lambda: self.deepseek.chat(self.conversation_history)
        )
        
        if response:
            # Extract the assistant's message
            assistant_message = response["choices"][0]["message"]["content"]
            
            # Add to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Use the TTS module to speak the response
            print(f"Assistant: {assistant_message}")
            await self.speak(assistant_message)
        else:
            error_message = "Sorry, I couldn't process that request. Please try again."
            print(f"Assistant: {error_message}")
            await self.speak(error_message)
        
        self.is_processing = False
    
    async def speak(self, text):
        """Asynchronous wrapper for the TTS service"""
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(
            None,
            lambda: self.tts_service.speak(text)
        )
    
    def clear_history(self):
        """Clear conversation history, keeping the system prompt"""
        self.conversation_history = [
            {"role": "system", "content": "You are a bilingual helpful assistant for a drone and robotics club. You speak arabic and english. Always respond in short and concise manner. Reply in english when asked in english and in arabic when asked in arabic."}
        ]
        print("Conversation history cleared.")
    
    async def listen_continuously(self):
        """Continuously listen for voice input in a non-blocking way"""
        print("Starting continuous listening...")
        await self.speak("Welcome to the Drone and Robotics Club assistant. I'm listening.")
        
        while not self.should_exit:
            if not self.is_processing:
                print("Listening...")
                
                # Run STT in a thread pool to avoid blocking the event loop
                loop = asyncio.get_event_loop()
                user_input = await loop.run_in_executor(
                    None,
                    lambda: transcribe_audio(duration=5)
                )
                
                if user_input and user_input.strip():
                    print(f"You said: {user_input}")
                    # Process in the background
                    asyncio.create_task(self.process_voice(user_input))
                
            # Small delay to prevent CPU overuse
            await asyncio.sleep(0.1)

async def main():
    """Main async function to run the voice assistant"""
    assistant = AsyncVoiceAssistant()
    
    print("Asynchronous Voice Assistant")
    print("============================")
    print("Speak to interact with the assistant")
    print("Say 'exit', 'quit', or 'goodbye' to end the session")
    print("Say 'clear history' or 'reset conversation' to start fresh")
    print("Press Ctrl+C to exit")
    print("============================")
    
    # Run the continuous listening loop
    await assistant.listen_continuously()

if __name__ == "__main__":
    # Run the async main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
