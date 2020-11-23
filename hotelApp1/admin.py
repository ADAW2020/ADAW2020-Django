from django.contrib import admin

# Register your models here.
from  hotelApp1 import models


admin.site.register(models.Habitacion)
admin.site.register(models.Reservas)
admin.site.register(models.tipoHabitacion)
admin.site.register(models.fechaXhabitacion)
admin.site.register(models.Consultar)
