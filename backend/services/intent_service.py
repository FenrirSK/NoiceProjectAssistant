import re 

def detect_intent(text: str) -> str:
    text = text.lower().strip()
    
    if re.search(r"\b(create|add|make|report)\b.*\b(snag|issue|problem|defect)\b", text):
        return "create_snag"
    
    if re.search(r"\b(search|find|show|look for)\b.*\b(snag|snags|issue|issues|problem|problems|defect|defects)\b", text):
        return "search_snags"
    
    if re.search(r"\b(delete|remove)\b", text):
        return "delete"
    
    if re.search(r"\b(update|edit|change|modify)\b", text):
        return "update"
    
    return "unknown"

