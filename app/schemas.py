from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

class ErrorResponse(BaseModel):
    error: str          # كود/اسم الخطأ
    message: str        # شرح مختصر
    details: dict | None = None  # تفاصيل اختيارية
