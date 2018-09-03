from django import forms

from .models import ProdutoCardapio

class ProdutoCardapioForm(forms.ModelForm):
    class Meta:
        model = ProdutoCardapio
        fields = ('nome', 'descricao', 'tamanhoEmPessoas','preco','tipoProduto','restaurante','foto',)
