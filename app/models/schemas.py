from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    """
    Modelo para la solicitud de chat.
    """
    messages: List[str]

class ChatResponse(BaseModel):
    """
    Modelo para la respuesta del chatbot.
    """
    response: str