from django.shortcuts import render
from hotelApp1 import models # traigo models para poder 
from .models import Habitacion

# Create your views here.
def home(request):
    return render(request, 'hotelApp1/home.html')

#-----------------------------------------------------------------

def registrar_cliente(request):
    if request.method == "POST":
        print("this was a POST")
         # si el request es post, voy a imprimir esto para verificar que el post se hizo
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['documento']
        fecha_nac = request.POST['fecha_nac']
        telefono = request.POST['telefono']
        password = request.POST['password']


        #ins es el comando que va a hacer la insercion de los datos en la base de datos
        ins = models.Clientes(nombre=nombre, apellido=apellido, dni=documento, fecha_nacimiento=fecha_nac, telefono=telefono, password=password)

        ins.save()  # este es el comando que graba los datos
        print("los datos han sido guardados en la base de datos")

    return render(request, 'hotelApp1/registrar-cliente.html')

#--------------------------------------------------------------------

def reservas(request):
    
    habitaciones = models.Habitacion.objects.all()
    context = {'habitaciones': habitaciones}

    return render(request, 'hotelApp1/reservas.html', context)