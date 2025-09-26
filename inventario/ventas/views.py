from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Categoria, Insumo
from django.shortcuts import render
from django.http import HttpResponse


class CategoriaListView(ListView):
    model = Categoria
    template_name = "categorias/list.html"
    context_object_name = "categorias"


class InsumoListView(ListView):
    model = Insumo
    template_name = "insumos/list.html"
    context_object_name = "insumos"

@login_required
def dashboard(request):
    context = {
        "total_categorias": Categoria.objects.count(),
        "total_insumos": Insumo.objects.count(),
        # "ultimos_movimientos": Movimiento.objects.order_by("-fecha")[:5],
        # "alertas_recientes": Alerta.objects.order_by("-id")[:5],
    }
    return render(request, "dashboard.html", context)

@login_required
def lotes_placeholder(request):
    return HttpResponse("<h3>Lotes</h3><p>Vista en construcción.</p>")

@login_required
def lotes_por_vencer_placeholder(request):
    return HttpResponse("<h3>Lotes por vencer</h3><p>Vista en construcción.</p>")

@login_required
def movimientos_placeholder(request):
    return HttpResponse("<h3>Movimientos</h3><p>Vista en construcción.</p>")

@login_required
def alertas_placeholder(request):
    return HttpResponse("<h3>Alertas</h3><p>Vista en construcción.</p>")