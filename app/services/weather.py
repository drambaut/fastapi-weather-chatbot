import requests
from fastapi import HTTPException
from app.core.config import settings

def get_weather(city: str) -> str:
    """
    Obtiene la información del clima de la API de OpenWeather.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return f"The current weather in {city} is {data['weather'][0]['description']} with a temperature of {data['main']['temp']}°C."
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise HTTPException(status_code=500, detail=f"Request error: {req_err}")