from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^promociones/$', views.promociones, name='promociones'),
    url(r'^reserva/$', views.nueva_reserva, name='reserva'),
    url(r'^turnos/$', views.selector_turnos),
    url(r'^confirmacion/$', views.confirmacion),
    url(r'^reserva_confirmada/$', views.reserva_confirmada),
]

