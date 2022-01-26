from django.http import HttpResponse
from django.shortcuts import render

from Dietetica.models import Cliente

def crear_clientes(request, apellido):
    clientes = Cliente (nombre="Python", apellido=apellido)
    clientes.save()

    return HttpResponse(f"Cliente listado {apellido}")

