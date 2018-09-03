from django.contrib import admin
from django.urls import path
from . import views
from cardapio import views as views_cardapio

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_restaurante, name='busca_restaurante'),
    path('cardapio/busca/', views_cardapio.busca_cardapio_por_restaurante, name='busca_cardapio_por_restaurante')
]
