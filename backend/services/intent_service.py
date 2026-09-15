import re


def detect_intent(text: str) -> str:

    text = text.lower().strip()

    # CREATE SNAG
    if re.search(
        r"\b("
        r"create|add|make|report|raise|log|"
        r"record|register|file"
        r")\b"
        r".*\b("
        r"snag|snags|issue|issues|problem|problems|"
        r"defect|defects"
        r")\b",
        text
    ):
        return "create_snag"

    # SEARCH SNAGS
    if re.search(
        r"\b("
        r"search|find|show|look\s+for|list|"
        r"give\s+me|are\s+there|is\s+there|"
        r"check|display"
        r")\b"
        r".*\b("
        r"snag|snags|issue|issues|problem|problems|"
        r"defect|defects"
        r")\b",
        text
    ):
        return "search_snags"

    # DELETE SNAG
    if re.search(
        r"\b(delete|remove|erase)\b",
        text
    ):
        return "delete"

    # UPDATE SNAG
    if re.search(
        r"\b("
        r"update|edit|change|modify|"
        r"assign|reassign|close|reopen"
        r")\b",
        text
    ):
        return "update"

    return "unknown"