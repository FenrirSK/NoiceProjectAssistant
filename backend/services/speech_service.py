import io
import re
import speech_recognition as sr

def normalize_speech(text: str) -> str:
    """
    fix common speech-recognition mistakes
    for words used in my project.
    """
    
    replacements = {
        r"\bsnake\b": "snag",
        r"\bsnack\b": "snag",
        r"\bsnakes\b": "snag",
        r"\bsnacks\b": "snag",
        r"\bsnap\b": "snag"
    }
    
    for pattern, replacement in replacements.items():
        text = re.sub(
            pattern,
            replacement,
            text,
            flags=re.IGNORECASE
        )
        
    return text

def speech_to_text(audio_bytes: bytes) -> str:
    """
    Convert audio data into text using Google Speech Recognition.
    """
    
    recognizer = sr.Recognizer()
    
    try:
        # Convert the audio bytes into an audio file object
        audio_file = io.BytesIO(audio_bytes)
        
        #Read the audio file
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            
        #Convert speech to text
        text = recognizer.recognize_google(audio)
        
        # Fix common speech-recognition mistakes
        text = normalize_speech(text)
        
        return text
    
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    
    except sr.RequestError:
        return "Speech recognition service is unavailable."
    
    except Exception as error:
        print(f"Speech recognition error: {error}")
        return "An error occurred while processing the audio"