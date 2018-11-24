# -*- coding: utf-8 -*-
from django.db import models
import restaurante.models
from decimal import Decimal

class Mesa(models.Model):
    numero = models.IntegerField()
    restaurante = models.ForeignKey(restaurante.models.Restaurante, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.numero)

class Comanda(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    inicio = models.DateTimeField(null=True)
    fim = models.DateTimeField(null=True)
    pago = models.BooleanField(default=0)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('login.Usuario', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.pk)

class Pedido(models.Model):
    quantidade = models.IntegerField(default=1)
    estado = models.IntegerField(default=0)
    coment = models.CharField(max_length=255, null=True)
    produto = models.ForeignKey('cardapio.ProdutoCardapio', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.pk)

class Cota(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    comanda = models.ForeignKey(Comanda, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return str(self.pk)
