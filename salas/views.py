from django.shortcuts import render_to_response
import datetime
from .models import Reserva
from django.views.decorators.csrf import csrf_exempt
from dateutil import parser
import google.oauth2.credentials
import googleapiclient.discovery
from django.http import JsonResponse
import google.oauth2.credentials


# Parametros
first_schedule = datetime.time(hour=12, minute=0)
final_schedule = datetime.time(hour=1, minute=0)
interval = 30
min_reserva = 60


def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})


def promociones(request):
    return render_to_response('promociones.html', context={"active": "promociones"})


@csrf_exempt
def reserva(request):
    schedule_options = []
    date = []
    action = 'Seleccionar'
    duration_hours = []
    first_schedule_date = []
    final_schedule_date = []
    post = []

    if request.GET:
        action = 'Actualizar'
        date = datetime.datetime.strptime(request.GET['fecha'], '%Y-%m-%d').date()

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

    if request.POST:
        post = "post"
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
        'reserva.html',
        context={
            "active": "reserva",
            "horarios": schedule_options,
            "date": date,
            "action": action,
            "tiempo": duration_hours,
            "from": first_schedule_date,
            "to": final_schedule_date,
            "post": post,
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


def sala(request):
    return render_to_response('sala.html', context={})


@csrf_exempt
def reservations(request):

    credentials_info = {'token': 'ya29.GltOBvriNoRcOGgILK5zbno3f-NxZvcqaSRQzSTEI1MFR_0olb0BCX66ysHDxjwd_iT5d_YzJ2LbVi1ogdIsMMQ5C7ftzM9QP8RByWO7HxgF1f3bx0yzo6EaDvqI',
                        'refresh_token': '1/_x4Yv7RM-IlVNrZjmH0dG7wVzEA15-UtTdyLQlhlAFlDJ1f38w7RHoYuXeCKSQIu',
                        'token_uri': 'https://www.googleapis.com/oauth2/v3/token',
                        'client_id': '828543267006-scihaocr3lbiq8pg9d0tsvjshccv8emc.apps.googleusercontent.com',
                        'client_secret': 'bJkZRIkr72sdUFsh3hD7hTif',
                        'scopes': ['https://www.googleapis.com/auth/calendar']}

    api_credentials = google.oauth2.credentials.Credentials(**credentials_info)
    calendar_api = googleapiclient.discovery.build('calendar', 'v3', credentials=api_credentials)

    if request.POST:
        event = {
            'summary': request.POST.get('title'),
            'start': {
                'dateTime': request.POST.get("start"),
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': request.POST.get("end"),
                'timeZone': 'America/Los_Angeles',
            },
        }
        event = calendar_api.events().insert(calendarId='ma2shcfl1bmfjrstv9bu732bn4@group.calendar.google.com',
                                             body=event)
        event.execute()
        return JsonResponse({})

    reservations = []

    from_date = datetime.datetime.fromtimestamp(int(request.GET.get("from"))/ 1e3).isoformat() + 'Z'
    to_date = datetime.datetime.fromtimestamp(int(request.GET.get("to"))/ 1e3).isoformat() + 'Z'

    # This is going to be saved in SALA object, harcoded now...
    events_result = calendar_api.events().list(calendarId='ma2shcfl1bmfjrstv9bu732bn4@group.calendar.google.com',
                                               timeMin=from_date, timeMax=to_date,
                                               maxResults=2500, singleEvents=True,
                                               orderBy='startTime').execute()

    for event in events_result.get('items', []):

        reservations.append({
          'id': event['id'],
          'title': event['summary'],
          'start': parser.parse(event['start']['dateTime']).astimezone().isoformat(),
          'end': parser.parse(event['end']['dateTime']).astimezone().isoformat(),
        })

    return JsonResponse({"events":reservations})

