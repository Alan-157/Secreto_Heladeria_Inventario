from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

    # ventas
    path("", include("ventas.urls")),
]
