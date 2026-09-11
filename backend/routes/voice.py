from fastapi import APIRouter, UploadFile, File
from services.speech_service import speech_to_text
from services.intent_service import detect_intent
from services.entity_service import extract_entities
from services.command_service import execute_command

router = APIRouter()


@router.post("/voice")
async def process_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    
    if not audio_bytes:
        return {
            "success": False,
            "message": "Audio file is empty"
        }
    
    # speech -> text
    text = speech_to_text(audio_bytes)
    
    # text -> intent
    intent = detect_intent(text)
    
    # text -> entities
    entities = extract_entities(text)
    
    return {
        "success": True,
        "text": text,
        "intent": intent,
        "entities": entities
    }