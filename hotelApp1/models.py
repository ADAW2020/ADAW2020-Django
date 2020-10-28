from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Clientes(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateTimeField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=32)
    password = models.CharField(max_length=250)


  
class Habitacion(models.Model):
    precio = models.IntegerField(default=100)    
    numero = models.IntegerField()
    tipo = models.CharField(max_length=250)

class tipoHabitacion(models.Model):
    descripcion = models.CharField(max_length=40)


class Reservas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_desde = models.CharField(max_length=250)
    fecha_hasta = models.DateTimeField(auto_now=False, auto_now_add=False)
    codigo_reserva = models.IntegerField(primary_key=True) # 1 => codigo reserva por default
    estado = models.CharField(max_length=250, default='activa')
    cant_huespedes = models.IntegerField()
    cant_habitaciones = models.IntegerField(default=1)
    



     
