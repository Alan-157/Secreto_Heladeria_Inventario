# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env en la raíz del proyecto
cp .env.example .env  # o crear manualmente

# Ejecutar migraciones
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Verificar conexión
docker compose exec web python manage.py check
