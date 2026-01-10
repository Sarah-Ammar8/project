from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Base Backend Service")
app.include_router(router)
