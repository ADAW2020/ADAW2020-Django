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
    disponible = models.BooleanField()
    tipo = models.ForeignKey(tipoHabitacion, on_delete=models.CASCADE)
    fecha_checking = models.DateField()
    fecha_checkout = models.DateField()
    

class Reservas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_desde = models.CharField(max_length=250)
    fecha_hasta = models.CharField(max_length=250)
    codigo_reserva = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #  codigo reserva por default autogenerado
    disponible = models.BooleanField()
    cant_huespedes = models.IntegerField()
    cant_habitaciones = models.IntegerField()
    precio_total = models.FloatField()
    #Habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cant_dias = models.IntegerField()
