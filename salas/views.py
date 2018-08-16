from django.shortcuts import render_to_response, render
import datetime
from .models import Reserva
from django.views.decorators.csrf import csrf_exempt
from dateutil import parser

# Parametros
first_schedule = datetime.time(hour=12, minute=0)
final_schedule = datetime.time(hour=1, minute=0)
interval = 30


def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})


def promociones(request):
    return render_to_response('promociones.html', context={"active": "promociones"})


@csrf_exempt
def reserva(request):
    schedule_options = []
    date = []
    action = 'Seleccionar'

    if request.POST:
        action = 'Actualizar'
        date = datetime.datetime.strptime(request.POST['fecha'], '%Y-%m-%d').date()

        first_schedule_date = datetime.datetime.combine(date, first_schedule)
        next_date = date + datetime.timedelta(days=1)
        final_schedule_date = datetime.datetime.combine(next_date, final_schedule)

        d = Reserva.objects.filter(reservation_date=date)
        disabled = []
        for r in d:
            desde = r.hora_inicio
            to = r.hora_fin
            while desde != to:
                disabled.append(desde)
                desde += datetime.timedelta(minutes=interval)

        h = first_schedule_date
        while h != final_schedule_date:
            if h in disabled:
                schedule_options.append((h, 'disabled'),)
            else:
                schedule_options.append((h, 'enabled'),)
            h += datetime.timedelta(minutes=interval)

    return render_to_response(
        'reserva.html',
        context={
            "active": "reserva",
            "horarios": schedule_options,
            "date": date,
            "action": action
        }
    )


@csrf_exempt
def confirmacion(request):
    rdict = request.POST.dict()
    rdate = rdict.pop('date')
    date = parser.parse(rdate).date()
    rlist = []
    for t in rdict:
        date_parse = parser.parse(t)
        rlist.append(date_parse)

    first_schedule_date = datetime.datetime.combine(date, first_schedule)

    while first_schedule_date not in rlist:
        first_schedule_date += datetime.timedelta(minutes=interval)

    duration_hours = len(rdict) * interval / 60
    final_schedule_date = first_schedule_date + datetime.timedelta(hours=duration_hours)

    return render_to_response(
        'confirmacion.html',
        context={
            "active": "reserva",
            "date": date,
            "tiempo": duration_hours,
            "from": first_schedule_date,
            "to": final_schedule_date
        }
    )


@csrf_exempt
def confirmada(request):
    reservation = Reserva()
    reservation.reservation_date = parser.parse(request.POST.get('date'))
    reservation.hora_inicio = parser.parse(request.POST.get('from'))
    reservation.hora_fin = parser.parse(request.POST.get('to'))
    reservation.sala = request.POST.get('sala')
    reservation.usuario = request.POST.get('user')
    reservation.save()

    return render_to_response('confirmada.html', context={"active": "reserva"})
