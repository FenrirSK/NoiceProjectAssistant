import re


def detect_intent(text: str) -> str:

    text = text.lower().strip()

    # Create snag
    if re.search(
        r"\b(create|add|make|report|raise|log)\b.*\b(snag|snags|issue|issues|problem|problems|defect|defects)\b",
        text
    ):
        return "create_snag"

    # Search snags
    if re.search(
        r"\b(search|find|show|look for|list|give me|are there|is there)\b.*"
        r"\b(snag|snags|issue|issues|problem|problems|defect|defects)\b",
        text
    ):
        return "search_snags"

    # Delete
    if re.search(
        r"\b(delete|remove)\b",
        text
    ):
        return "delete"

    # Update
    if re.search(
        r"\b(update|edit|change|modify)\b",
        text
    ):
        return "update"

    return "unknown"
