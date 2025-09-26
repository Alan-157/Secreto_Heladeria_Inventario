from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("categorias/", views.CategoriaListView.as_view(), name="categorias_list"),
    path("insumos/", views.InsumoListView.as_view(), name="insumos_list"),

    # Placeholders para evitar NoReverseMatch
    path("lotes/", views.lotes_placeholder, name="lotes_list"),
    path("lotes/por-vencer/", views.lotes_por_vencer_placeholder, name="lotes_por_vencer"),
    path("movimientos/", views.movimientos_placeholder, name="movimientos_list"),
    path("alertas/", views.alertas_placeholder, name="alertas_list"),
]
