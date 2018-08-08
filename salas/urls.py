from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^promociones/$', views.promociones, name='promociones'),
    url(r'^reserva/$', views.reserva, name='reserva'),
    url(r'^reserva/turnos/$', views.turnos),
    url(r'^reserva/confirmacion/$', views.confirmacion),
    url(r'^reserva/confirmada/$', views.confirmada),
]