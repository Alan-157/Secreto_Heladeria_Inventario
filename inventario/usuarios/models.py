from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # AbstractUser ya trae: username, password, first_name, last_name, email, etc.
    # Forzamos email único porque lo usaremos para recuperar contraseña.
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    class Rol(models.TextChoices):
        ADMIN = "ADMIN", "Administrador"
        GESTOR = "GESTOR", "Gestor"
        VISOR = "VISOR", "Visualizador"

    rol = models.CharField(max_length=20, choices=Rol.choices, default=Rol.GESTOR)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"


class UserPerfil(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_perfiles"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.nombre


class UserPerfilAsignacion(models.Model):
    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    perfil  = models.ForeignKey(UserPerfil, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_perfil_asignacion"
        unique_together = ("usuario", "perfil")
        verbose_name = "Asignación de perfil"
        verbose_name_plural = "Asignaciones de perfiles"

    def __str__(self):
        return f"{self.usuario} → {self.perfil}"
