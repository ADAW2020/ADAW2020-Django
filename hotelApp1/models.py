from django.db import models
from django.contrib.auth.models import User

# Create your models here.
  
class Habitacion(models.Model):
    precio = models.IntegerField(default=100)    
    numero = models.IntegerField()
    tipo = models.CharField(max_length=250)

class tipoHabitacion(models.Model):
    descripcion = models.CharField(max_length=40)


class Reservas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_desde = models.CharField(max_length=250)
    fecha_hasta = models.CharField(max_length=250)
    codigo_reserva = models.AutoField(primary_key=True) # 1 => codigo reserva por default
    estado = models.CharField(max_length=250, default='activa')
    cant_huespedes = models.IntegerField()
    cant_habitaciones = models.IntegerField(default=1)
    precio_total = models.FloatField()
    
