# Generated by Django 2.0.7 on 2018-07-12 00:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='turnos',
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_final',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 7, 11, 21, 22, 30, 530327), null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_inicio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 7, 11, 21, 22, 30, 530327), null=True),
        ),
    ]
