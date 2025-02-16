from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat import process_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Endpoint para manejar las solicitudes de chat con el asistente de clima.
    """
    try:
        response_text = process_chat(request.messages)
        return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
