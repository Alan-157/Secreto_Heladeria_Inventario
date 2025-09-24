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

class Categoria(BaseModel):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

