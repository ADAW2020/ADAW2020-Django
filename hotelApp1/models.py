from django.db import models
from django.contrib.auth.models import User
import uuid
import hotel.settings
import datetime
from django import forms

# Create your models here.

class tipoHabitacion(models.Model):
    descripcion = models.CharField(max_length=40)
  


class Habitacion(models.Model):
    precio = models.IntegerField()    
    numero = models.IntegerField()
    tipo = models.ForeignKey(tipoHabitacion, on_delete=models.CASCADE)
    
class fechaXhabitacion(models.Model):
    f_checking = models.DateField()
    f_checkout = models.DateField()
    numero_habitacion = models.IntegerField()
    


class Reservas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_desde = models.CharField(max_length=250)
    fecha_hasta = models.CharField(max_length=250)
    codigo_reserva = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #  codigo reserva por default autogenerado
    cant_huespedes = models.IntegerField()
    cant_habitaciones = models.IntegerField()
    precio_total = models.FloatField()
    cant_dias = models.IntegerField()
    #Habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

class Consultar(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Telefono = models.IntegerField()
    email = models.CharField(max_length=40)
    Consulta = models.CharField(max_length=120)