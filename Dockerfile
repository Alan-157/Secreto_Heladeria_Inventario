FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . /code/
