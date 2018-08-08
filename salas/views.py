from django.shortcuts import render_to_response, render
import datetime
from .models import Reserva
from django.views.decorators.csrf import csrf_exempt


def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})


def promociones(request):
    return render_to_response('promociones.html', context={"active": "promociones"})


def reserva(request):
    return render_to_response(
        'form_reserva.html',
    )


@csrf_exempt
def turnos(request):
    date = datetime.datetime.strptime(request.POST['fecha'], '%Y-%m-%d').__format__('%d/%m/%Y')
    turn_options = (
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18:30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
    )

    return render_to_response(
        'turnos.html',
        context={
            "active": "reserva",
            "horarios": turn_options,
            "date": date,
        }
    )


@csrf_exempt
def confirmacion(request):
    horarios = dict(request.POST)
    date = horarios.pop("date")[0]
    desde = datetime.timedelta(hours=12, minutes=00)
    desde_str = str(desde)[0:5]

    while desde_str not in horarios:
        desde += datetime.timedelta(minutes=30)
        desde_str = str(desde)[0:5]

    tiempo = (len(horarios) - 1) / 2
    hasta = desde + datetime.timedelta(hours=tiempo)
    hasta_str = str(hasta)[0:5]

    return render_to_response(
        'confirmacion.html',
        context={
            "active": "reserva_confirmada",
            "date": date,
            "tiempo": tiempo,
            "desde_str": desde_str,
            "hasta_str": hasta_str
        }
    )


@csrf_exempt
def confirmada(request):
    reserva = Reserva()
    reserva.dia = datetime.datetime.strptime(request.POST['fecha'], '%d/%m/%Y').date()
    reserva.hora_inicio = request.POST.get('inicio')
    reserva.hora_fin = request.POST.get('fin')
    reserva.sala = request.POST.get('sala')
    reserva.usuario = request.POST.get('user')
    reserva.save()

    return render_to_response('confirmada.html', context={"active": "reserva_confirmada"})
