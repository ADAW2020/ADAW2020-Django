from django.shortcuts import render, redirect
from hotelApp1 import models  # traigo models para poder
from .models import Habitacion
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Reservas, Habitacion
import datetime
from logging import Logger
import re
#from django.contrib.sessions.models import Session
# Create your views here.

def home(request):
    habitaciones = models.Habitacion.objects.all()
    context = {'habitaciones': habitaciones}

    tipo_habitaciones = models.tipoHabitacion.objects.all()

    context['tipo_habitaciones'] = tipo_habitaciones

    return render(request, 'hotelApp1/home.html', context)

# -----------------------------------------------------------------

def registrar_cliente(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                usuario = User.objects.get(username=request.POST['usuario'])
                return render(request, 'hotelApp1/registrar-cliente.html', {'error': 'ese usuario ya existe'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['usuario'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'hotelApp1/registrar-cliente.html', {'error': 'los passwords deben coincidir'})
    else:
        # User wants to enter info
        return render(request, 'hotelApp1/registrar-cliente.html')


# --------------------------------------------------------------------

def ingresar(request):

    if request.method == 'POST':
        usuario = auth.authenticate(
            username=request.POST['usuario'], password=request.POST['password'])
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('home')
        else:
            return render(request, 'hotelApp1/ingresar.html', {'error': 'El usuario o password son incorrectos'})

    else:
        return render(request, 'hotelApp1/ingresar.html')

# ---------------------------------------------------------------------


def salir(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


# --------------------------------------------------------------------

def reservas(request):

    tipo_habitaciones = models.tipoHabitacion.objects.all()
    context = {'tipo_habitaciones': tipo_habitaciones}

    # form = FirstForm(request.POST)
    pickerR = request.POST.get('pickerR', None)

    # con esto capturo los datos del primer form
    pickerL = request.POST.get('pickerL', None)

    cantH = (request.POST.get('cant_huespedes'))

    context['pickerR'] = pickerR

    context['pickerL'] = pickerL 

    context['cantidad_huespedes'] = (cantH)
    
    cantHabitaciones = int(request.POST.get('cant_habitaciones'))
    
    context['cantHabitaciones'] = cantHabitaciones

    c = pickerL[:2]
    d = pickerR[:2]

    dias = int(c)-int(d)  

    context['dias'] = dias

 

    precioTotal = cantHabitaciones * dias *100
    
    context['precioTotal'] = precioTotal
    
    num_habitacion = 0



    return render(request, 'hotelApp1/reservas.html', context)

    if request.method == 'POST' and request.user.is_authenticated():
        reservas = Reservas()
        reservas.cant_huespedes = cantH
        reservas.fecha_hasta = pickerR
        reservas.fecha_desde = pickerL
        reservas.cant_habitaciones = cantHabitaciones
        reservas.cant_dias = dias
        reservas.precio_total = precioTotal
        reservas.disponible = True
        reservas.usuario = request.user

        ins1 = Reservas(cant_huespedes=cantH,fecha_desde=pickerL, fecha_hasta=pickerR, cant_habitaciones=cantHabitaciones,
        cant_dias=dias, precio_total=precioTotal, disponible=True,usuario=request.user) 

       # ins.save()
    else:
       return render({'mensaje':'Debe loguearse para poder reservar.'})

       
    
    return render(request, 'hotelApp1/reservas.html', {'confirmacion':'La reserva ha sido generada'})


#-------------------------------------------------------------------------------

def confirmacion(request):
    return render(request, 'hotelApp1/confirmacion.html')