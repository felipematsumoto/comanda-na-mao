from django.db import models
from decimal import Decimal

class TipoProduto(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome.encode('utf8','replace')

class ProdutoCardapio(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    foto = models.FileField(upload_to='fotosCardapio/')
    tamanhoEmPessoas = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    tipoProduto = models.ForeignKey(TipoProduto, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome.encode('utf8','replace')

class ProdutoRestaurante(models.Model):
    produtoCardapio = models.ForeignKey(ProdutoCardapio, on_delete=models.CASCADE)
    restaurante = models.ForeignKey('restaurante.Restaurante', on_delete=models.CASCADE)
    class Meta:
        unique_together = (("produtoCardapio", "restaurante"),)
