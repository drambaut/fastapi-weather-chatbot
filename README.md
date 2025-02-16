# FastAPI Weather Chatbot

## Overview
This project is a FastAPI-based chatbot that provides weather information using the OpenWeather API. It integrates LangChain SDK for AI-powered conversations and maintains a chat history for user interactions.

## Features
- **Chat Interface**: Communicate with the AI assistant via a RESTful API.
- **Weather Queries**: Get current, forecast, and historical weather data for any location.
- **AI-Powered Responses**: Uses LangChain SDK to generate intelligent responses.
- **FastAPI Framework**: Built with FastAPI for high performance and scalability.
- **Docker Support**: Easily deployable with Docker and Docker Compose.

## Project Structure
```
fastapi-weather-chatbot/
│── app/
│   ├── api/v1/routes.py       # API endpoints
│   ├── core/config.py         # Application settings
│   ├── services/chat.py       # Chat processing logic
│   ├── services/weather.py    # OpenWeather API integration
│   ├── models/schemas.py      # Request/response data models
│   ├── main.py                # Application entry point
│── tests/
│   ├── test_chat.py           # Unit tests for chat service
│   ├── test_weather.py        # Unit tests for weather service
│── .env                       # Environment variables
│── .gitignore                 # Git ignore file
│── Dockerfile                 # Docker image configuration
│── docker-compose.yml         # Docker Compose setup
│── requirements.txt           # Python dependencies
│── README.md                  # Project documentation
```

## Installation
### Prerequisites
- Python 3.10+
- Docker (optional, for containerized deployment)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/fastapi-weather-chatbot.git
   cd fastapi-weather-chatbot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenWeather API key:
   ```ini
   OPENWEATHER_API_KEY=your_api_key_here
   ```

## Running the Application
### Locally
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Using Docker
```sh
docker-compose up --build
```

## API Endpoints
### Chat Endpoint
- **URL**: `/api/v1/chat`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "messages": ["What is the weather in New York?"]
  }
  ```
- **Response**:
  ```json
  {
    "response": "The current weather in New York is clear sky with a temperature of 25.5°C."
  }
  ```

## Running Tests
```sh
pytest tests/
```