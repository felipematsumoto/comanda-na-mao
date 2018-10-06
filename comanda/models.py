# -*- coding: utf-8 -*-
from django.db import models
import restaurante.models

class Mesa(models.Model):
    numero = models.IntegerField()
    restaurante = models.ForeignKey(restaurante.models.Restaurante, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.numero)

class Comanda(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)
    idusuario = models.IntegerField()
    def __str__(self):
        return str(self.pk)