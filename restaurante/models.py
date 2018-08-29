from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome.encode('utf8','replace')
