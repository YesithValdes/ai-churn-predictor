# 1. Imagen base: Usamos una versión ligera de Python 3.11
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalamos dependencias del sistema necesarias para psycopg2 y herramientas de red
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 4. Copiamos el archivo de requerimientos e instalamos las librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos todo el código de tu proyecto al contenedor
COPY . .

# 6. Exponemos el puerto donde corre FastAPI
EXPOSE 8000

# 7. Comando para arrancar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]