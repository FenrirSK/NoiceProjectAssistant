import re


def extract_entities(text: str) -> dict:

    text = text.lower().strip()

    entities = {
        "location": None,
        "issue": None,
        "assignee": None,
        "status": None
    }

    # --------------------------------
    # Extract location
    # --------------------------------

    location_match = re.search(
        r"\b(?:in|at|for)\s+(?:the\s+)?(.+?)"
        r"(?=\s+(?:and|assign|assigned|with|status|to|as)\b|$)",
        text
    )

    if location_match:
        entities["location"] = location_match.group(1).strip()
        
    # --------------------------------
    # Extract location from update command
    # --------------------------------

    update_location_match = re.search(
        r"\b(?:update|change|edit|modify)\s+"
        r"(?:the\s+)?(.+?)\s+snag\b",
        text
    )

    if update_location_match:
        entities["location"] = update_location_match.group(1).strip()    
        
        
    # --------------------------------
    # Extract location from delete command
    # --------------------------------

    delete_location_match = re.search(
        r"\b(?:delete|remove)\s+"
        r"(?:the\s+)?(.+?)\s+snag\b",
        text
    )

    if delete_location_match:
        entities["location"] = delete_location_match.group(1).strip()

    # --------------------------------
    # Extract issue
    # --------------------------------

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

    # --------------------------------
    # Extract assignee
    # --------------------------------

    assign_match = re.search(
        r"\b(?:assign(?:ed)?\s+to)\s+"
        r"(?:the\s+)?(.+?)"
        r"(?=\s+(?:in|at|for|with|status|to|as)\b|$)",
        text
    )

    if assign_match:

        entities["assignee"] = assign_match.group(1).strip()

    # --------------------------------
    # Extract status
    # --------------------------------

    if re.search(r"\bopen\b", text):

        entities["status"] = "open"

    elif re.search(r"\bclosed\b", text):

        entities["status"] = "closed"

    elif re.search(r"\bin progress\b", text):

        entities["status"] = "in progress"

    return entities