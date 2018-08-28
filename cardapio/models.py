from django.db import models

class TipoProduto(models.Model):
    nome = models.Charfield(max_length=50)
    def __str__(self):
        return self.nome.encode('utf8','replace')

class ProdutoCardapio(models.Model):
    nome = models.Charfield(max_length=50)
    descricao = models.Charfield(max_length=255)
    foto = models.FileField(upload_to='fotosCardapio')
    tipoProduto = models.ForeignKey(TipoProduto)
    def __str__(self):
        return self.nome.encode('utf8','replace')
