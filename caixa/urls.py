from django.urls import path
from . import views

urlpatterns = [
    path('caixa/', views.envia_comandas_em_aberto, name='abre_mesa'),
    path('mostra_pedido/',views.mostra_pedido, name='pega_pedido'),
    path('fecha_pedido/',views.fecha_pedido, name='fecha_pedido'), #fecha comanda
    path('mesa/',views.envia_mesas, name='envia_mesas')
]
