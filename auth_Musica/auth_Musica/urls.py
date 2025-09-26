
from django.contrib import admin
from django.http import request
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('usuario.urls')),
    path('', lambda request: redirect('/auth/register/')),
    # path('musicas/', include('musicas.urls')),
]
