from django.shortcuts import render, redirect
from hotelApp1 import models  # traigo models para poder
from .models import Habitacion
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Reservas
import datetime
# Create your views here.


def home(request):
    habitaciones = models.Habitacion.objects.all()
    context = {'habitaciones': habitaciones}
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

    #cantH = request.POST.get('cant_huespedes', None)

    cantH = request.POST['cant_huespedes']

    context['pickerR'] = pickerR

    context['pickerL'] = pickerL 

    context['cant_huespedes'] = cantH

    c = pickerL[:2]
    d = pickerR[:2]

    dias = int(c)-int(d)  


    cant_dias ={'dias':dias}

    context['dias'] = cant_dias

    precioTotal = cantH
    
    if context['tipo_habitaciones'] == 'simple' and cantH < 4:
        precioTotal = cantH*120*20*dias
    elif context['tipo_habitaciones'] == 'doble':
        precioTotal = cantH*120*30*dias
    elif context['tipo_habitaciones'] == 'triple':
        precioTotal = cantH*120*40*dias
    
    print(precioTotal)
    
    #context['precio_total'] = precioTotal

    if request.method == 'POST':
        reservas = Reservas()
        reservas.cant_huespedes = request.POST['cant_huespedes']
        reservas.fecha_hasta = request.POST['pickerR']
        reservas.fecha_desde = request.POST['pickerL']

   # else:

    return render(request, 'hotelApp1/reservas.html', context)
    