import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings:
    """
    Configuración global de la aplicación.
    """
    PROJECT_NAME: str = "FastAPI Weather Chatbot"
    API_VERSION: str = "v1"
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY")
    
    if not OPENWEATHER_API_KEY:
        raise ValueError("Error: La variable de entorno OPENWEATHER_API_KEY no está configurada.")

# Instancia de configuración global
settings = Settings()