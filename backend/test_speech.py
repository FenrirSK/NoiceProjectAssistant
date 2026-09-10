from services.speech_service import speech_to_text

def main():
    print("==================================")
    print("   Speech Recognition Test")
    print("==================================")
    print()
    
    audio_path = input("Enter the path of your audio file: ")
    
    try:
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            
        text = speech_to_text(audio_bytes)
        
        print()
        print("Recognized text:", text)
        
    except FileNotFoundError:
        print("Audio file not found:")
    except Exception as error:
        print(f"Error: {error}")
        
if __name__ == "__main__":
    main()
    
    
    