from django.db import models

# Create your models here.
class Administradores(models.Model):
    nombre = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    dni_admin = models.IntegerField(primary_key=True)

class Clientes(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField(primary_key=True)
    fecha_nacimiento = models.DateTimeField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=32)
    password = models.CharField(max_length=250)

  
class Habitacion(models.Model):
    numero = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)    



class Reservas(models.Model):
    dni_cliente = models.ForeignKey(Clientes, default=None, on_delete=models.CASCADE)
    fecha_desde = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_hasta = models.DateTimeField(auto_now=False, auto_now_add=False)
    codigo_reserva = models.IntegerField(primary_key=True, default=1) # 1 => codigo reserva por default
    estado = models.CharField(max_length=250, default='activa')
    numero_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cant_huespedes = models.IntegerField(default=1)


     
