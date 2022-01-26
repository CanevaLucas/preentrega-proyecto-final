

from django.contrib import admin
from django.urls import path

from Proyecto1.views import hoy, saludo, saludar_a, clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/", saludo),
    path("hoy/", hoy),
    path("mi_nombre/<nombre>", saludar_a),
    path("template/", clientes),

]

#python manage.py runserver