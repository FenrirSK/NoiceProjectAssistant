import io
import speech_recognition as sr

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
        
        return text
    
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    
    except sr.RequestError:
        return "Soeech recognition service is unavailable."
    
    except Exception as error:
        print(f"Speech recognition error: {error}")
        return "An error occured while processing the audio"