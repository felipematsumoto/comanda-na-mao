from django.contrib import admin
from django.urls import path
from . import views
from cardapio import views as views_cardapio
from .views import add_restaurante
from .views import msg
from .views import lista_restaurantes
from .views import leitura_restaurante
from .views import busca_restaurante_id

urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca_restaurante, name='busca_restaurante'),
    path('cardapio/busca/', views_cardapio.busca_cardapio_por_restaurante, name='busca_cardapio_por_restaurante'),
    path('msg/',msg, name= "msg"),
    path('add_restaurante/',add_restaurante, name= "add_restaurante"),
    path('lista/',lista_restaurantes, name= "lista"),
    path('leitura_restaurante/',leitura_restaurante, name= "leitura_restaurante"),
    path('busca_id/',busca_restaurante_id, name= "busca_restaurante_id")
]
