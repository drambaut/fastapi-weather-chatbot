from fastapi import FastAPI
from app.api.v1 import api_router

def create_app() -> FastAPI:
    """
    Crea y configura la instancia de la aplicación FastAPI.
    """
    app = FastAPI(title="FastAPI Weather Chatbot", version="1.0")
    
    app.include_router(api_router, prefix="/api")
    
    return app