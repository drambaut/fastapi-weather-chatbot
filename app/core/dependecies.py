from fastapi import Depends
from app.core.config import settings

def get_settings():
    """
    Dependencia para obtener la configuración global de la aplicación.
    """
    return settings
