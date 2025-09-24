from django.db import models

class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo")
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)  # se asigna al crear
    updated_at = models.DateTimeField(auto_now=True)      # se actualiza cada vez que se guarda
    deleted_at = models.DateTimeField(null=True, blank=True)  # opcional para borrado lógico

class Usuario(BaseModel):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    ROLES = [
        ("ADMIN", "Administrador"),
        ("GESTOR", "Gestor"),
        ("VISOR", "Visualizador")
    ]
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"

