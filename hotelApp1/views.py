from django.shortcuts import render, redirect
from hotelApp1 import models # traigo models para poder 
from .models import Habitacion
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #formulario para autenticar que viene con django
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    habitaciones = models.Habitacion.objects.all()
    context = {'habitaciones': habitaciones}
    return render(request, 'hotelApp1/home.html', context)

#-----------------------------------------------------------------

def ingresar(request):

    if request.method == 'POST':
        nombre_usuario = request.POST['usuario']
        password = request.POST['password']

        usuario = auth.authenticate(usuario=nombre_usuario, password=password)
        if usuario is not None:
            auth.login(request,usuario)
            return redirect("home.html")

    else:
        messages.info(request, 'Credenciales invalidas')
        #return redirect('ingresar.html')  


    
    return render(request, 'hotelApp1/ingresar.html')



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
        print("usuario registrado")
        return redirect('registrar.html')

    return render(request, 'hotelApp1/registrar-cliente.html')

#--------------------------------------------------------------------

def reservas(request):
    
    habitaciones = models.Habitacion.objects.all()
    context = {'habitaciones': habitaciones}
    
    #form = FirstForm(request.POST)
    pickerR = request.POST.get('pickerR', None)
    
    pickerL = request.POST.get('pickerL', None) #con esto capturo los datos del primer form

    context['pickerR'] = pickerR

    context['pickerL'] = pickerL

    print(context)

    return render(request, 'hotelApp1/reservas.html', context)