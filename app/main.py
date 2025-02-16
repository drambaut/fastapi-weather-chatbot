import uvicorn
from fastapi import FastAPI
from app.api.v1 import api_router

def create_app() -> FastAPI:
    """
    Crea y configura la instancia de la aplicación FastAPI.
    """
    app = FastAPI(title="FastAPI Weather Chatbot", version="1.0", debug=True)  # Activar Debug
    
    # Registrar los routers de la API
    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)