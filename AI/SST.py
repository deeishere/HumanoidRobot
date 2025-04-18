# Libraries
import whisper
import sounddevice as sd
import tempfile
import wavio
import os

# Loading the model (use "small" or "medium" for better multilingual support)
modelStt = whisper.load_model("small")  # Better language support than "base"

# Recording Audio
def record_audio(duration=5, fs=44100):
    print("Recording....")
    audio = sd.rec(int(duration*fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Recording complete.")
    
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    wavio.write(temp_file.name, audio, fs, sampwidth=2)
    print(f"Audio file saved at: {temp_file.name}")
    return temp_file.name
    
# Audio Transcription with language support
def transcribe_audio(duration=5, language=None):
    audio_file = record_audio(duration=duration)
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")
    
    print(f"Transcribing file: {audio_file}")
    
    # Configure transcription options
    options = {
        "fp16": False,  # Use FP16 if you have a compatible GPU
    }
    
    # Add language option if specified
    if language:
        options["language"] = language
    else:
        # Auto-detect language (Whisper is good at this)
        options["task"] = "transcribe"
    
    result = modelStt.transcribe(audio_file, **options)
    
    detected_language = result.get("language", "unknown")
    print(f"Detected language: {detected_language}")
    
    # Clean up
    try:
        os.unlink(audio_file)
    except:
        pass
    
    return result['text']

# Optional function to specifically detect the language first
def detect_language(audio_file):
    # Load audio
    audio = whisper.load_audio(audio_file)
    audio = whisper.pad_or_trim(audio)
    
    # Make log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(modelStt.device)
    
    # Detect language
    _, probs = modelStt.detect_language(mel)
    detected_lang = max(probs, key=probs.get)
    
    return detected_lang

# Example usage
if __name__ == "__main__":
    print("Speak in English or Arabic...")
    
    # Auto-detect language
    transcription = transcribe_audio(duration=5)
    print(f"Transcription: {transcription}")
    
    # Or specify language for better accuracy
    # transcription = transcribe_audio(duration=5, language="ar")
    # print(f"Arabic Transcription: {transcription}")
