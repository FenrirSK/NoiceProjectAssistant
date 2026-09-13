from database.connection import db


def execute_command(intent: str, entities: dict):

    if intent == "create_snag":
        return create_snag(entities)

    if intent == "search_snags":
        return search_snags(entities)

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
        "success": True,
        "message": "Snag created successfully",
        "snag_id": str(result.inserted_id),
        "snag": snag
    }


def search_snags(entities: dict):

    query = {}

    if entities.get("location"):
        query["location"] = entities["location"]

    if entities.get("issue"):
        query["issue"] = entities["issue"]

    if entities.get("assignee"):
        query["assignee"] = entities["assignee"]

    snags = list(db.snags.find(query))

    for snag in snags:
        snag["_id"] = str(snag["_id"])

    return {
        "success": True,
        "count": len(snags),
        "snags": snags
    }