from django.shortcuts import render_to_response
from salas.forms import Date
import datetime

# Create your views here.


def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})


def promociones(request):
    return render_to_response('promociones.html', context={"active":"promociones"})


def nueva_reserva(request):
    form = Date()
    return render_to_response('form_reserva.html', context={"active":"reserva", "form": form})


def selector_turnos(request):
    date = datetime.date(int(request.GET['date_year']),int(request.GET['date_month']), int(request.GET['date_day'])).strftime('%m/%d/%Y')

    horarios = (
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
        'selector_turnos.html',
        context={
            "active": "reserva",
            "horarios": horarios,
            "date": date,
        }
    )


def confirmacion(request):
    date = request.GET['date']
    horarios = dict(request.GET)
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
            "active": "confirmacion",
            "date": date,
            "tiempo": tiempo,
            "desde_str": desde_str,
            "hasta_str": hasta_str,
        }
    )


def reserva_confirmada(request):
    return render_to_response('reserva_confirmada.html', context={"active": "reserva_confirmada"})