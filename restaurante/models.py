from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=155)
    foto = models.FileField(upload_to='fotosRestaurante/')
    tipoCozinha = models.CharField(max_length=50)
    # SEMANA = (
    #        ('Dom', 'Segunda'),
    #        ('Seg', 'Segunda'),
    #        ('Ter', 'Segunda'),
    #        ('Qua', 'Segunda'),
    #        ('Qui', 'Segunda'),
    #        ('Sex', 'Segunda'),
    #        ('Sab', 'Segunda'))


    
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

