# Usa la imagen oficial de Python 3.10 como base
FROM python:latest

# Establece la variable de entorno PYTHONUNBUFFERED en 1 para evitar la creación de archivos pycache
ENV PYTHONUNBUFFERED 1

# Configura la base de datos PostgreSQL
# ENV DB_HOST=db
# ENV DB_PORT=5432
# ENV DB_NAME=mydatabase
# ENV DB_USER=mydatabaseuser
# ENV DB_PASSWORD=mypassword

# Crea y establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app/
COPY . /app/
