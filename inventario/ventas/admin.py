# ventas/admin.py
from django.contrib import admin
from .models import Categoria, Insumo

admin.site.register(Categoria)
admin.site.register(Insumo)
