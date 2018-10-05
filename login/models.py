# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from comanda import models as comanda_models


class TipoConta(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)
    tipoUser = models.ForeignKey(TipoConta, on_delete=models.CASCADE, null=True)
    comanda = models.IntegerField(default=-1)#Coloca -1 caso nao inserido
    mesa = models.IntegerField(default=-1)#Coloca -1 caso nao inserido
    # Tirar as referencias de chave para insercao, perdi um tempo desgracado com isso
    def __str__(self):
        return self.login
