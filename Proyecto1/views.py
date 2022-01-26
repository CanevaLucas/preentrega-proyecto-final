
from django.template.context import Context
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.template import Template
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import loader

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

    diccionario= {f"nombre": "Lucas"}

    plantilla = loader.get_template("clientes.html")
   
    documento = plantilla.render (diccionario)
    
    return HttpResponse(documento)

    # Diccionario = {
    #     "Nombre": "Martin",
    #     "Apellido": "Caneva"}

    # Context = context(Diccionario)
    
    # return render (request, "clientes.html")
