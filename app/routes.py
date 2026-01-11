from fastapi import APIRouter
from .services import get_health_status, get_item
from .schemas import HealthResponse

router = APIRouter()

@router.get("/")
def root():
    return {"service": "base-backend", "docs": "/docs"}

@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(status=get_health_status())

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return get_item(item_id)
