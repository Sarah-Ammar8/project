from .errors import NotFoundError

def get_health_status() -> str:
    return "ok"

def get_item(item_id: int) -> dict:
    # مثال عام بدون فكرة محددة
    if item_id != 1:
        raise NotFoundError(details={"item_id": item_id})
    return {"id": 1, "name": "example"}
