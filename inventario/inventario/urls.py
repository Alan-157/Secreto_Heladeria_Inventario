from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vistas simples que ya tenías
@login_required
def dashboard(request): return render(request, "dashboard.html")
@login_required
def insumos_list(request): return render(request, "insumos/list.html")
@login_required
def categorias_list(request): return render(request, "categorias/list.html")
@login_required
def lotes_list(request): return render(request, "lotes/list.html")
@login_required
def lotes_por_vencer(request): return render(request, "lotes/por_vencer.html")
@login_required
def movimientos_list(request): return render(request, "movimientos/list.html")
@login_required
def alertas_list(request): return render(request, "alertas/list.html")

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include(("usuarios.urls"), namespace="accounts")),

    # Aliases cómodos sin romper el namespace
    path("login/",    RedirectView.as_view(pattern_name="accounts:login",    permanent=False), name="login"),
    path("logout/",   RedirectView.as_view(pattern_name="accounts:logout",   permanent=False), name="logout"),
    path("register/", RedirectView.as_view(pattern_name="accounts:register", permanent=False), name="register"),
    path("password/reset/", RedirectView.as_view(
        pattern_name="accounts:password_reset", permanent=False
    ), name="password_reset"),
    path("password/change/", RedirectView.as_view(
        pattern_name="accounts:password_change", permanent=False
    ), name="password_change"),

    # Dashboard y listas
    path("", dashboard, name="dashboard"),
    path("insumos/", insumos_list, name="insumos_list"),
    path("categorias/", categorias_list, name="categorias_list"),
    path("lotes/", lotes_list, name="lotes_list"),
    path("lotes/por-vencer/", lotes_por_vencer, name="lotes_por_vencer"),
    path("movimientos/", movimientos_list, name="movimientos_list"),
    path("alertas/", alertas_list, name="alertas_list"),
]
