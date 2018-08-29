from django.contrib import admin

from .models import TipoProduto, ProdutoCardapio, ProdutoRestaurante

admin.site.register(TipoProduto)
admin.site.register(ProdutoCardapio)
admin.site.register(ProdutoRestaurante)
