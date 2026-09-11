import re

def extract_entities(text: str) -> dict:
    text = text.lower().strip()
    
    entities = {
        "location": None,
        "issue": None,
        "assignee": None
    }
    
    # Extract location
    location_match = re.search(
        r"\b(?:in|at|for)\s+(?:the\s+)?(.+?)(?:\s+(?:and|assign|assigned)\b|$)",
        text
    )
    
    if location_match:
        entities["location"] = location_match.group(1).strip()
        
    # Extract common issue
    issue_words = [
        "ceiling",
        "wall",
        "floor",
        "door",
        "window",
        "leak",
        "paint",
        "plumbing",
        "electrical"
    ]
    
    for issue in issue_words:
        if issue in text:
            entities["issue"] = issue
            break
        
    # Extract assignee
    assign_match = re.search(
        r"\bassign(?:ed)?\s+(?:it\s+)?to\s+(?:the\s+)?(.+?)(?:\s*$)",
        text
    )
    
    if assign_match:
        entities["assignee"] = assign_match.group(1).strip()
        
    return "entities"