# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from comanda import models as comanda_models
from decimal import Decimal


class TipoConta(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return str(self.nome)

class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=20)
    tipoUser = models.ForeignKey(TipoConta, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.login)
