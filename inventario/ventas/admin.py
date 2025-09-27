from django.contrib import admin
from .models import (
    Categoria, Insumo, ReglaAlerta, InsumoReglaAlerta,
    Sucursal, Area, Ubicacion, Movimiento
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion","estado")
    search_fields = ("nombre",)
    list_filter = ("estado",)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("nombre","categoria","unidad_medida","stock_actual","stock_minimo","stock_maximo","estado")
    search_fields = ("nombre","categoria__nombre")
    list_filter = ("categoria","estado")
    ordering = ("nombre",)
    list_select_related = ("categoria",)

@admin.register(ReglaAlerta)
class ReglaAlertaAdmin(admin.ModelAdmin):
    list_display = ("nombre","severidad","estado")
    list_filter = ("severidad","estado")

@admin.register(InsumoReglaAlerta)
class InsumoReglaAlertaAdmin(admin.ModelAdmin):
    list_display = ("insumo","regla_alarma","umbral_min","umbral_max")
    list_filter = ("regla_alarma__severidad",)
    list_select_related = ("insumo","regla_alarma")

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre","estado")
    list_filter = ("estado",)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("nombre","sucursal","estado")
    list_filter = ("sucursal","estado")
    list_select_related = ("sucursal",)

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ("nombre","codigo","sucursal","area","estado")
    list_filter = ("sucursal","area","estado")
    list_select_related = ("sucursal","area")

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    date_hierarchy = "fecha"
    list_display = ("fecha","tipo","insumo","cantidad","unidad","sucursal","area","ubicacion")
    list_filter = ("tipo","sucursal","area","ubicacion")
    ordering = ("-fecha",)
    list_select_related = ("insumo","sucursal","area","ubicacion")
