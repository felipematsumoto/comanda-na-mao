# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)
    nomeDono = models.CharField(max_length=50)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=50)
    foto = models.FileField(upload_to='static/restaurante/fotosRestaurante/')
    email = models.CharField(max_length=50)
    dono = models.ForeignKey('login.Usuario', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome
