from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.IntegerField()
    nomeDono = models.CharField(max_length=50)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)
    foto = models.FileField(upload_to='static/restaurante/fotosRestaurante/')
    email = models.CharField(max_length=50)


    def __str__(self):
        return self.nome
