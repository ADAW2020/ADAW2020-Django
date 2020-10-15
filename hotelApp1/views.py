from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'hotelApp1/home.html')



def registrar_cliente(request):
    return render(request, 'hotelApp1/registrar-cliente.html')