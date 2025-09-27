# Motor de base de datos
MySQL

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

# Como cargar las semillas
docker compose exec web python manage.py seed_inventario
docker compose exec web python manage.py seed_lacteos
docker compose exec web python manage.py seed_naranja

# Crear admin
docker compose exec web python manage.py createsuperuser
Usuario: admin
Clave: admin123

# Acceder con docker
Frontend: http://localhost:8000
Admin de Django: http://localhost:8000/admin/
