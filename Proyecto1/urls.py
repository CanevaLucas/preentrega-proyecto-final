

from django.contrib import admin
from django.urls import path
from Dietetica.models import Cliente
from Dietetica.views import crear_clientes

from Proyecto1.views import hoy, saludo, saludar_a, clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/", saludo),
    path("hoy/", hoy),
    path("mi_nombre/<nombre>", saludar_a),
    path("template/", clientes),
    path("clientes/<nombre>", crear_clientes)


]

#python manage.py runserver