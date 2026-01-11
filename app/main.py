from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .config import APP_NAME
from .routes import router
from .errors import AppError
from .schemas import ErrorResponse

app = FastAPI(title=APP_NAME)
app.include_router(router)

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    # خرائط بسيطة حسب نوع الخطأ
    status_code = 400
    if exc.error == "NOT_FOUND":
        status_code = 404

    payload = ErrorResponse(error=exc.error, message=exc.message, details=exc.details).model_dump()
    return JSONResponse(status_code=status_code, content=payload)

@app.exception_handler(Exception)
async def unhandled_error_handler(request: Request, exc: Exception):
    # لا تفضحي تفاصيل الخطأ للمستخدم في الإنتاج
    payload = ErrorResponse(error="INTERNAL_ERROR", message="Unexpected server error").model_dump()
    return JSONResponse(status_code=500, content=payload)
