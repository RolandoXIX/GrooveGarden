# Generated by Django 2.0.7 on 2018-07-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0009_auto_20180713_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='horarios',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
