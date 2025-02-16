FROM python:3.10

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de inicio de la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]