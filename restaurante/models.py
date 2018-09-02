from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharFiel(max_length=255)
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
<<<<<<< HEAD
        return self.nome.encode('utf8','replace')


=======
        return self.nome
>>>>>>> 5e08017cb09c5f864a16eb0e9d25f6c71f419de4
