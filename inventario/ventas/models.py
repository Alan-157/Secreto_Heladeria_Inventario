from django.db import models

class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo")
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True  #Solo se define una vez como abstracta

class Categoria(BaseModel):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

class Insumo(BaseModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="insumos", null=True, blank=True)
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

class ReglaAlerta(BaseModel):
    SEVERIDADES = [
        ("GRAVE","Grave"), 
        ("ALTA","Alta"), 
        ("MEDIA","Media")
    ]
    nombre = models.CharField(max_length=100, unique=True)
    severidad = models.CharField(max_length=10, choices=SEVERIDADES)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.severidad})"

class InsumoReglaAlerta(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="reglas")
    regla_alarma = models.ForeignKey(ReglaAlerta, on_delete=models.CASCADE, related_name="insumos")
    umbral_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    umbral_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ("insumo", "regla_alarma")

    def __str__(self):
        return f"{self.insumo} ↔ {self.regla_alarma}"

class Sucursal(BaseModel):
    nombre = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.nombre

class Area(BaseModel):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="areas")
    nombre = models.CharField(max_length=150)

    class Meta:
        unique_together = ("sucursal","nombre")

    def __str__(self):
        return f"{self.sucursal} / {self.nombre}"

class Ubicacion(BaseModel):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="ubicaciones")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="ubicaciones")
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo or 's/c'})"

class Movimiento(BaseModel):
    TIPOS = [("ENTRADA","Entrada"), ("SALIDA","Salida"), ("AJUSTE","Ajuste")]
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="movimientos")
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=10, choices=TIPOS)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=20, default="unid")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.fecha:%Y-%m-%d %H:%M} {self.tipo} {self.insumo} {self.cantidad}{self.unidad}"