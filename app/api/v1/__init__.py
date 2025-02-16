from fastapi import APIRouter
from app.api.v1.routes import router as chat_router

api_router = APIRouter()

# Registrar las rutas
api_router.include_router(chat_router, tags=["chat"])
