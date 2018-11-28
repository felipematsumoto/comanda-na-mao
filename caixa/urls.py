from django.urls import path
from . import views

urlpatterns = [
    path('caixa/', views.envia_comandas_com_pedidos_para_caixa, name='envia1'),
    path('mostra_pedido/',views.mostra_pedido, name='pega_pedido'),
    path('fecha_pedido/',views.fecha_pedido, name='fecha_pedido') #fecha comanda
]
