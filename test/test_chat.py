from fastapi.testclient import TestClient
from app.main import app
from app.models.schemas import ChatRequest

# Crear cliente de pruebas
client = TestClient(app)

def test_chat_endpoint():
    """
    Prueba el endpoint de chat con un mensaje de ejemplo.
    """
    request_data = ChatRequest(messages=["What is the weather in New York?"])
    response = client.post("/api/v1/chat", json=request_data.dict())
    
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)