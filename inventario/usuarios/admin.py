from django.contrib import admin
from .models import Usuario, UserPerfil, UserPerfilAsignacion

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id","username","email","rol","is_active","is_staff")
    search_fields = ("username","email")
    list_filter = ("rol","is_active","is_staff")

@admin.register(UserPerfil)
class UserPerfilAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","descripcion","created_at","updated_at")
    search_fields = ("nombre",)

@admin.register(UserPerfilAsignacion)
class UserPerfilAsignacionAdmin(admin.ModelAdmin):
    list_display = ("id","usuario","perfil","created_at")
    list_select_related = ("usuario","perfil")
    search_fields = ("usuario__username","perfil__nombre")
