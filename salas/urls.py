from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^promociones/$', views.promociones, name='promociones'),
    url(r'^reserva/$', views.reserva, name='reserva'),
    url(r'^reserva/confirmada/$', views.confirmada),
    url(r'^sala/$', views.sala, name='sala'),
    url(r'^reservations/$', views.reservations, name='reservations'),
    #url(r'^oauthcallback/$', views.oauthcallback, name='oauthcallback'),
]