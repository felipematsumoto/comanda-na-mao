from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=140)
    cozinha = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
