"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.shortcuts import render

def dashboard(request): return render(request, "dashboard.html")
def insumos_list(request): return render(request, "insumos/list.html")
def categorias_list(request): return render(request, "categorias/list.html")
def lotes_list(request): return render(request, "lotes/list.html")
def lotes_por_vencer(request): return render(request, "lotes/por_vencer.html")
def movimientos_list(request): return render(request, "movimientos/list.html")
def alertas_list(request): return render(request, "alertas/list.html")

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("insumos/", insumos_list, name="insumos_list"),
    path("categorias/", categorias_list, name="categorias_list"),
    path("lotes/", lotes_list, name="lotes_list"),
    path("lotes/por-vencer/", lotes_por_vencer, name="lotes_por_vencer"),
    path("movimientos/", movimientos_list, name="movimientos_list"),
    path("alertas/", alertas_list, name="alertas_list"),
]