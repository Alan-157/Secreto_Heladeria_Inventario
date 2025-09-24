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

    class Meta:
        abstract = True  # no crea tabla, solo se hereda

class Insumo(BaseModel):
    nombre = models.CharField(max_length=150)
    stock_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    stock_maximo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unidad_medida = models.CharField(max_length=50, null=True, blank=True)
    costo_unitario = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.unidad_medida})"

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ['nombre']




