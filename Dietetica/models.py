
from django.db.models import Model
from django.db.models.fields import BooleanField, CharField, DateField, EmailField, IntegerField

# Create your models here.
# camada = IntegerField()


class Cliente(Model):
    
     nombre = CharField(max_length=30)
     apellido = CharField(max_length=40)
     email = EmailField()
     telefono = IntegerField()

class Porveedor(Model):

     empresa = CharField(max_length=30)
     telefono = IntegerField()
     direccion = CharField(max_length=40)

class Productos(Model):

     tipo = CharField(max_length=30)
     marca = IntegerField()
     precio = IntegerField()
     codigo = CharField(max_length=30)

class Empleados(Model):

     nombre = CharField(max_length=40)
     apellido = CharField(max_length=40)
     dni = IntegerField()
     email = EmailField()
     direccion = CharField(max_length=40)
     telefono = IntegerField()
     fecha_de_cobro = DateField()
     estado = BooleanField()
