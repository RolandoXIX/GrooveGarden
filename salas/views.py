from django.shortcuts import render_to_response, render
import datetime
from django.shortcuts import redirect
from .models import Reserva

def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})

def promociones(request):
    return render_to_response('promociones.html', context={"active":"promociones"})

def reserva(request):
    if request.GET:
        date = datetime.datetime.strptime(request.GET.get('fecha'), "%Y-%m-%d").date().__format__('%Y/%m/%d')
        return redirect(date)
    else:
        return render_to_response(
            'form_reserva.html',
        )

def selector_turnos(request, year, month, day):
    date = f'{day}/{month}/{year}'
    turnos = (
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
    if request.GET:
        horarios = dict(request.GET)
        desde = datetime.timedelta(hours=12, minutes=00)
        desde_str = str(desde)[0:5]
        while desde_str not in horarios:
            desde += datetime.timedelta(minutes=30)
            desde_str = str(desde)[0:5]

        tiempo = (len(horarios) - 1) / 2
        hasta = desde + datetime.timedelta(hours=tiempo)
        hasta_str = str(hasta)[0:5]

        url = 'confirmation/' + 'desde=' + desde_str + 'tiempo=' + str(tiempo)
        return redirect(url)

    else:
        return render_to_response(
            'selector_turnos.html',
            context={
                "active": "reserva",
                "horarios": turnos,
                "date": date,
            }
        )


def confirmacion(request, year, month, day, desde, tiempo):
    if request.method == "POST":
        date = request.POST.get('fecha')
        time = request.POST.get('duracion')
        minutes = int(float(tiempo) * 60)
        sala = request.POST.get('sala')
        user = request.POST.get('user')
        reserva = Reserva()

        for d in range(0, minutes):
            reserva.sala = sala
            reserva.dia = date
            reserva.usuario = user
            reserva.horario = time + datetime.timedelta(minutes=d)
            d += 30
            reserva.save()

        return render(request, 'reserva_confirmada.html', context={"active": "reserva_confirmada"})

    else:
        date = f'{day}/{month}/{year}'
        time_hour = int(desde[:2])
        time_minute = int(desde[3:])
        time = datetime.timedelta(hours=time_hour, minutes=time_minute)
        hasta = time + datetime.timedelta(hours=float(tiempo))
        hasta_str = str(hasta)[:5]
        return render_to_response(
            'confirmacion.html',
            context={
                "active": "reserva_confirmada",
                "date": date,
                "tiempo": tiempo,
                "desde_str": desde,
                "hasta_str": hasta_str
            }
        )


def reserva_confirmada(request):
    return render_to_response('reserva_confirmada.html', context={"active": "reserva_confirmada"})