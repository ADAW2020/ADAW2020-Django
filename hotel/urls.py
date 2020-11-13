"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import hotelApp1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hotelApp1.views.home, name='home'),
    path('ingresar.html/',hotelApp1.views.ingresar, name='ingresar'),
    path('registrar-cliente.html/',hotelApp1.views.registrar_cliente, name='registrar-cliente'),
    path('reservas.html/', hotelApp1.views.reservas, name='reservas'),
    path('salir.html/', hotelApp1.views.salir, name='salir'),
    path('',include("django.contrib.auth.urls")),
    path('confirmacion.html/',hotelApp1.views.confirmacion, name='confirmacion'),
    path('no_disponibilidad.html',hotelApp1.views.no_disponibilidad, name='no_disponibilidad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += staticfiles_urlpatterns()
