from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=11, blank=True, null=True)
    nomeDono = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    endereco = models.CharField(max_length=50)


    def __str__(self):
        return self.nome
