from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^promociones/$', views.promociones, name='promociones'),
    url(r'^reserva/$', views.reserva, name='reserva'),
    url(r'^turnos/$', views.selector_turnos),
    url(r'^confirmacion/$', views.confirmacion),
    url(r'^reserva_confirmada/$', views.reserva_confirmada),
    url(r'^reserva/(\d{4})/(\d{2})/(\d{2})/$', views.selector_turnos),
    url(r'^reserva/(\d{4})/(\d{2})/(\d{2})/confirmation/desde=(\d{2}:\d{2})tiempo=(\d{1}.\d{1})/$', views.confirmacion),
    ]

