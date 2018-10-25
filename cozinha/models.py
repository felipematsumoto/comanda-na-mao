from django.db import models

# Create your models here.
from django.db import models
from decimal import Decimal

class Historico_de_Pedidos(models.Model):
    custo = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    estado = models.IntegerField(default=0)
    coment = models.CharField(max_length=255)
    produto = models.ForeignKey('cardapio.ProdutoCardapio', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.pk)

class Aux_form(models.Model):
    IDaux = models.IntegerField()
    transicao = models.IntegerField()
