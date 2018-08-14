from django.db import models


class Sala(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)

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
    sala = models.CharField(max_length=50)
    reservation_date = models.DateField()
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.sala


