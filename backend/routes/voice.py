from fastapi import APIRouter, UploadFile, File
from services.speech_service import speech_to_text
from services.intent_service import detect_intent
from services.entity_service import extract_entities
from services.command_service import execute_command
from utils.confirmation import (
    needs_confirmation,
    create_confirmation_message,
    is_confirmation,
    is_rejection,
    set_pending_command,
    get_pending_command,
    clear_pending_command
)

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
    
    # check if the user is confirming a previous command
    print("CONFIRMATION TEST TEXT:", repr(text))
    if is_confirmation(text):
        
        pending_intent, pending_entities = get_pending_command()
        
        if pending_intent:
            
            command_result = execute_command(
                pending_intent,
                pending_entities
            )
            
            clear_pending_command()
            
            return{
                "success": True,
                "text": text,
                "intent": pending_intent,
                "entities": pending_entities,
                "confirmation_required": False,
                "command": command_result
            }
            
    # check if the user rejected a previous command
    if is_rejection(text):
        
        pending_intent, pending_entities = get_pending_command()
        
        if pending_intent:
            
            clear_pending_command()
            
            return {
                "success": True,
                "text": text,
                "intent": pending_intent,
                "entities": pending_entities,
                "confirmation_required": False,
                "command": {
                    "success": False,
                    "message": "Action cancelled"
                }                 
            }
    
    # text -> intent
    intent = detect_intent(text)
    
    # text -> entities
    entities = extract_entities(text)
    
    # check whether confirmation is required
    if needs_confirmation(intent):
        
        set_pending_command(intent, entities)
        
        confirmation_message = create_confirmation_message(
            intent,
            entities
        )
    
        return {
            "success": True,
            "text": text,
            "intent": intent,
            "entities": entities,
            "confirmation_required": True,
            "confirmation_message": confirmation_message
        }
    
    # execute command directly if confirmation is not required
    command_result = execute_command(intent, entities)

    return {
        "success": True,
        "text": text,
        "intent": intent,
        "entities": entities,
        "command": command_result
    }