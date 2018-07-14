from django.db import models
from django.utils.timezone import datetime, timedelta


class Sala(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)

    def __str__(self):
        return self.nombre


class Horarios(models.Model):
    DIAS = (
        ('0', 'LUNES'),
        ('1', 'MARTES'),
        ('2', 'MIERCOLES'),
        ('3', 'JUEVES'),
        ('4', 'VIERNES'),
        ('5', 'SABADO'),
        ('6', 'DOMINGO')
    )
    dia = models.CharField(max_length=1, choices=DIAS)

    HORARIOS = (
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30')
    )

    horarios = models.CharField(max_length=5, choices=HORARIOS)

    def __str__(self):
        return '%s - %s' % (self.dia, self.horarios)


class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)
    dia = models.DateField()

    def horarios():
        hora = timedelta(hours=0, minutes=0)
        horarios = []
        for i in range(0, 1440, 30):
            horarios.append((i, hora))
            hora += timedelta(minutes=30)
        return horarios

    horarios = models.CharField(max_length=4, choices=horarios() )

    def __str__(self):
        return '%s - %s' % (self.sala, self.dia)


