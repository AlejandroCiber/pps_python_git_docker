# Imagen base
FROM python:3.11-slim

WORKDIR /app

# Copiamos requirements y la app
COPY requirements.txt .
COPY . .

# Instalamos las dependencias directamente en el sistema
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]

