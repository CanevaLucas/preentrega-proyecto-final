
from contextvars import Context
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django import template
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from django.template import Template, context

from django.template import context

def saludo(request):
    return HttpResponse ("<h1>Bienvenido a la Dietetica<h1>")

def hoy(request):
    hoy= datetime.now()
    return HttpResponse (f"Hoy es {hoy}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def clientes(request):
    
    lista_de_notas=[2,2,3,7,2,5]

    diccionario = {"nombre":"apellido"}

    miHtml = open ("C:\Users\Luke\Documents\PYTHON\Pre entrega proyecto final\mi_proyecto\preentrega-proyecto-final\Dietetica\templates/clientes.html")

    plantilla = template(miHtml.read())

    miHtml.close()

    miContexto = context(diccionario)

    documento = plantilla.render (miContexto)

    return HttpResponse(documento)

    # Diccionario = {
    #     "Nombre": "Martin",
    #     "Apellido": "Caneva"}

    # Context = context(Diccionario)
    
    # return render (request, "clientes.html")
