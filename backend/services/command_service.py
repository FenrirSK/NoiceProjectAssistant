from database.connection import db

def execute_command(intent: str, entities: dict):
    if intent == "create_snag":
        return create_snag(entities)
    
    return {
        "success": False,
        "message": f"Unknown intent: {intent}"
    }
    
def create_snag(entities: dict):
    snag = {
        "location": entities.get("location"),
        "issue": entities.get("issue"),
        "assignee": entities.get("assignee"),
        "status": "open"
    }
    
    result = db.snags.insert_one(snag)
    
    return {
        "succes": True,
        "issue": "Snag created successfully",
        "snag_id": str(result.inserted_id),
        "snag": "snag"
    }