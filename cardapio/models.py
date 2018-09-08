# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class TipoProduto(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class ProdutoCardapio(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
#<<<<<<< HEAD
    foto = models.FileField(upload_to='static/cardapio/fotosCardapio/')
#=======
    foto = models.FileField(upload_to='fotosCardapio/')
#>>>>>>> 5e08017cb09c5f864a16eb0e9d25f6c71f419de4
    tamanhoEmPessoas = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    tipoProduto = models.ForeignKey(TipoProduto, on_delete=models.SET_NULL, null=True)
    restaurante = models.ForeignKey('restaurante.Restaurante', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
