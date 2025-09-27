from django.core.management.base import BaseCommand
from ventas.models import Categoria, Insumo

class Command(BaseCommand):
    help = "Carga insumos de la categoría Lácteos"

    def handle(self, *args, **kwargs):
        # Crear categoría Lácteos
        cat_lacteos, _ = Categoria.objects.get_or_create(nombre="Lácteos")

        # Crear insumos
        Insumo.objects.get_or_create(
            nombre="Leche Entera",
            categoria=cat_lacteos,
            stock_minimo=10,
            stock_maximo=100,
            unidad_medida="litros",
            costo_unitario=850
        )

        Insumo.objects.get_or_create(
            nombre="Mantequilla",
            categoria=cat_lacteos,
            stock_minimo=5,
            stock_maximo=40,
            unidad_medida="kg",
            costo_unitario=3200
        )

        Insumo.objects.get_or_create(
            nombre="Yogurt Natural",
            categoria=cat_lacteos,
            stock_minimo=8,
            stock_maximo=60,
            unidad_medida="litros",
            costo_unitario=1100
        )

        self.stdout.write(self.style.SUCCESS("Insumos de Lácteos cargados correctamente"))
