from django.shortcuts import render, redirect
from hotelApp1 import models  # traigo models para poder
from .models import Habitacion, fechaXhabitacion
from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Reservas, Habitacion, Consultar
import datetime
from logging import Logger
import re
from django.http import HttpResponseRedirect
from datetime import date
from datetime import datetime
import pickle
import random
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

#---------------------------------------------------------------------

def consultar(request):

    if request.method == 'POST':
        consultar = Consultar.objects.all()
        nombre = str(request.POST.get('nombre',None))
        ape = str(request.POST.get('apellido',None))
        tel = request.POST.get('telefono',None)
        email = str(request.POST.get('email',None))
        consulta = str(request.POST.get('consulta',None))

        ins3 = Consultar(Nombre=nombre, Apellido=ape, Telefono=tel, email=email, Consulta=consulta)
        ins3.save()
        return render(request, 'hotelApp1/consultar.html', {'mensaje': 'la consulta ha sido enviada. Nos contactaremos a la brevedad'})



    
    return render(request, 'hotelApp1/consultar.html')



# --------------------------------------------------------------------

def info(request):
    
    return render(request, 'hotelApp1/info.html')



# --------------------------------------------------------------------

def imagenes(request):
    
    return render(request, 'hotelApp1/imagenes.html')



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

def no_disponibilidad(request):
    return render(request, 'hotelApp1/no_disponibilidad.html')
# --------------------------------------------------------------------

def reservas(request):

    pickerR = request.POST.get('pickerR', None)
    
    pickerR_checkout = datetime.strptime(pickerR, '%d/%m/%Y').date() #convierto la fecha de tipo string a datetime
   
    pickerL = request.POST.get('pickerL', None)
    
    pickerL_checking = datetime.strptime(pickerL, '%d/%m/%Y').date()  #convierto la fecha de tipo string a datetime

    th = request.POST.get('tipo_hab', None)
    
    #import pdb; pdb.set_trace()

    fechaXhabitaciones = fechaXhabitacion.objects.all()
    
    if pickerL == pickerR:
        return render(request, 'hotelApp1/fechas_erroneas.html')


    for h in fechaXhabitaciones:
         if h.f_checking <= pickerL_checking and pickerR_checkout <= h.f_checkout and h.numero_habitacion != None:             
            return render(request, 'hotelApp1/no_disponibilidad.html')

    cantHabitaciones = int(request.POST.get('cant_habitaciones'))
    
    cantH = request.POST.get('cantidad_huespedes')
    
    tipo_habitaciones = models.tipoHabitacion.objects.all()

    #tip_h = models.tipoHabitacion.objects.filter(descripcion=th)
      
    context_reservas = {'tipo_habitaciones': tipo_habitaciones}
    context_reservas['pickerR'] = pickerR
    context_reservas['pickerL'] = pickerL
    context_reservas['cant_huespedes'] = cantH
    context_reservas['cantHabitaciones'] = cantHabitaciones
    context_reservas['plc'] = pickerL_checking
    context_reservas['prc'] = pickerR_checkout
    context_reservas['tipoh'] = th
    
    dias2 = pickerR_checkout - pickerL_checking

    fecha_actual = datetime.now().date()
    
    if dias2.days*(-1) < 0 and pickerL_checking < datetime.now().date or pickerL_checking < datetime.now().date():
        return render(request, 'hotelApp1/fechas_erroneas.html')

    context_reservas['dias'] = dias2.days*(-1)
    
    if th == "simple":
        precioTotal = cantHabitaciones * dias2.days*(-1) *100
    
    if th == "doble":
         precioTotal = cantHabitaciones * dias2.days*(-1) *150
    
    if th == "triple":
        precioTotal = cantHabitaciones * dias2.days*(-1) *200
    
    context_reservas['precioTotal'] = precioTotal
    
    num_habitacion = 0
    

    if request.method == 'POST':
        print(0)          

    else:
                return render({'mensaje':'Debe loguearse para poder reservar.'})
                    
      
    with open('context_reservas.pkl', 'wb') as crpickle:
        pickle.dump(context_reservas, crpickle)

    
    return render(request, 'hotelApp1/reservas.html', context_reservas)
#-------------------------------------------------------------------------------

def confirmacion(request):
   
    with open('context_reservas.pkl', 'rb') as crpickle:
        datos_reserva = pickle.load(crpickle)
    print(datos_reserva)
    
    cantH = datos_reserva['cant_huespedes']
    pickerL = datos_reserva['pickerL']
    pickerR = datos_reserva['pickerR']
    cantHabitaciones = datos_reserva['cantHabitaciones']
    dias = datos_reserva['dias']
    precioTotal = datos_reserva['precioTotal']
    pickerL_checking = datos_reserva['plc']
    pickerR_checkout = datos_reserva['prc']
    tipo_h = datos_reserva['tipoh']
    
    if request.user.is_authenticated:
        ins1 = Reservas(cant_huespedes=cantH,fecha_desde=pickerL, fecha_hasta=pickerR, cant_habitaciones=cantHabitaciones,
                    cant_dias=dias, precio_total=precioTotal, usuario=request.user, tipo_habitacion=tipo_h) 
                #import pdb; pdb.set_trace()
        ins1.save()   
        habitacion_aleatoria = random.randint(1,6)
        fechaXhabitaciones = fechaXhabitacion.objects.all()
        ins2 = fechaXhabitacion(f_checkout=pickerR_checkout, f_checking=pickerL_checking, numero_habitacion=habitacion_aleatoria)
        ins2.save()
        return render(request, 'hotelApp1/confirmacion.html')
    else:
        return render(request, 'hotelApp1/error_no_logueado.html')



#--------------------------------------------------------------

def mi_cuenta(request):
        
     Usuario = request.user
     reserva = Reservas.objects.all()
     fd = []
     fh = []
     ch = []
     cr = []
     pt = []
     th = []
     
     for ru in reserva:
         if ru.usuario == Usuario:
            cr.append(ru.codigo_reserva)
            fd.append(ru.fecha_desde)
            fh.append(ru.fecha_hasta)
            pt.append(ru.precio_total)
            ch.append(ru.cant_habitaciones)
            th.append(ru.tipo_habitacion)
     
     codigos_reserva = models.Reservas.objects.filter(usuario=Usuario)
     fecha_desde = models.Reservas.objects.filter(usuario=Usuario)
     fecha_hasta = models.Reservas.objects.filter(usuario=Usuario)
     precio_total = models.Reservas.objects.filter(usuario=Usuario)
     canth = models.Reservas.objects.filter(usuario=Usuario)
     cantd = models.Reservas.objects.filter(usuario=Usuario)
     tipo_h = models.Reservas.objects.filter(usuario=Usuario)

        
     Context = {'codigos_reserva': codigos_reserva}
     Context['fecha_desde']= fecha_desde
     Context['fecha_hasta']= fecha_hasta
     Context['precio_total']=precio_total
     Context['canth']=canth
     Context['cantd']=cantd 
     Context['tipo_h'] = tipo_h 
     return render(request,'hotelApp1/mi_cuenta.html', Context)

#--------------------------------------------------------------
def fechas_erroneas(request):
    
    return render(request,'hotelApp1/fechas_erroneas.html')
#--------------------------------------------------------------

def error_no_logueado(request):
    
    return render(request,'hotelApp1/error_no_logueado.html')


def mapa_de_sitio(request):

    return render(request,'hotelApp1/mapa_de_sitio.html')