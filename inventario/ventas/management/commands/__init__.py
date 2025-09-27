from django.core.management.base import BaseCommand
from ventas.models import Categoria, Insumo, ReglaAlerta, Sucursal, Area, Ubicacion

class Command(BaseCommand):
    help = "Carga datos de ejemplo para inventario"

    def handle(self, *args, **kwargs):
        # Categorías
        cat_helados, _ = Categoria.objects.get_or_create(nombre="Helados")
        cat_toppings, _ = Categoria.objects.get_or_create(nombre="Toppings")

        # Insumos
        Insumo.objects.get_or_create(
            nombre="Frutilla",
            categoria=cat_helados,
            stock_minimo=5,
            stock_maximo=50,
            unidad_medida="kg",
            costo_unitario=1200
        )

        Insumo.objects.get_or_create(
            nombre="Chocolate",
            categoria=cat_toppings,
            stock_minimo=2,
            stock_maximo=30,
            unidad_medida="kg",
            costo_unitario=1500
        )

        # Reglas de alerta
        ReglaAlerta.objects.get_or_create(nombre="Stock Crítico", severidad="GRAVE")
        ReglaAlerta.objects.get_or_create(nombre="Stock Bajo", severidad="ALTA")

        # Sucursal y área
        sucursal, _ = Sucursal.objects.get_or_create(nombre="Sucursal Coquimbo")
        area, _ = Area.objects.get_or_create(sucursal=sucursal, nombre="Producción")

        # Ubicación
        Ubicacion.objects.get_or_create(sucursal=sucursal, area=area, nombre="Bodega Principal", codigo="BOD-001")

        self.stdout.write(self.style.SUCCESS("Datos de inventario cargados correctamente"))
