from django.contrib import admin
from .models import Sala, Reserva, Horarios

# usuario: admin
# clave: admin833

admin.site.register(Sala)
admin.site.register(Horarios)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'dia', 'hora_inicio', 'hora_fin')
