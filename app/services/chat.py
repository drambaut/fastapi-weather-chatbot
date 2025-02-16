from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from app.services.weather import get_weather
import os
import re

# Asegurar que la clave API existe
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("Error: OPENAI_API_KEY no está configurado.")

llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Historial de conversación
conversation_history = []

def process_chat(messages: list) -> str:
    """
    Procesa la conversación con LangChain y verifica si se solicita información del clima.
    """
    global conversation_history
    
    user_message = messages[-1].strip()
    
    # Agregar mensajes previos a la conversación
    chat_messages = [SystemMessage(content="You are a helpful weather assistant.")]
    chat_messages.extend(conversation_history)
    chat_messages.append(HumanMessage(content=user_message))

    # 🔹 Detectar si se solicita información del clima
    match = re.search(r"weather in ([a-zA-Z\s]+)", user_message, re.IGNORECASE)

    if match:
        city = match.group(1).strip()  # Extraer solo la ciudad
        weather_info = get_weather(city)

        # 🔹 Generar respuesta con LangChain incorporando la información meteorológica
        system_prompt = (
            f"You are a helpful weather assistant. A user has asked about the weather in {city}. "
            f"Here is the latest weather update: {weather_info}. "
            "Now, generate a natural response incorporating this information."
        )

        chat_messages.append(SystemMessage(content=system_prompt))

    # 🔹 Generar la respuesta final con LLM
    response_text = llm.predict("\n".join([msg.content for msg in chat_messages]))

    # Guardar en historial
    conversation_history.append(HumanMessage(content=user_message))
    conversation_history.append(AIMessage(content=response_text))
    
    return response_text