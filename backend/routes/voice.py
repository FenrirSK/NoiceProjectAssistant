from fastapi import APIRouter, UploadFile, File
from services.speech_service import speech_to_text

router = APIRouter()


@router.post("/voice")
async def process_voice(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    
    if not audio_bytes:
        return {
            "success": False,
            "message": "Audio file is empty"
        }
    
    text = speech_to_text(audio_bytes)
    
    return {
        "success": True,
        "text": text
    }