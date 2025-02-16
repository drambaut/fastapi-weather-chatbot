import pytest
from fastapi import HTTPException
from app.services.weather import get_weather

def test_get_weather(mocker):
    """
    Prueba la función get_weather simulando una respuesta de la API de OpenWeather.
    """
    mock_response = {
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 25.5}
    }
    
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))
    
    city = "New York"
    response = get_weather(city)
    
    assert "clear sky" in response
    assert "25.5°C" in response

def test_get_weather_invalid_city(mocker):
    """
    Prueba la función get_weather con una ciudad inválida.
    """
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=404))
    
    with pytest.raises(HTTPException) as exc_info:
        get_weather("InvalidCity")
    
    assert exc_info.value.status_code == 404