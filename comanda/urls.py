from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicia_comanda/', views.inicia_comanda, name='inicia_comanda'),
    path('libera_comanda/', views.libera_comanda, name='libera_comanda')
]
