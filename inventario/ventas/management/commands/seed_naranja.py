from django.core.management.base import BaseCommand
from ventas.models import Categoria, Insumo

class Command(BaseCommand):
    help = "Carga el insumo Naranja en la categoría Frutas"

    def handle(self, *args, **kwargs):
        # Crear categoría Frutas si no existe
        cat_frutas, _ = Categoria.objects.get_or_create(nombre="Frutas")

        # Crear insumo Naranja
        Insumo.objects.get_or_create(
            nombre="Naranja",
            categoria=cat_frutas,
            stock_minimo=15,
            stock_maximo=80,
            unidad_medida="kg",
            costo_unitario=950
        )

        self.stdout.write(self.style.SUCCESS("Insumo Naranja cargado correctamente"))
