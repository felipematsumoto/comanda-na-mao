from django.forms import ModelForm

from .models import Pedido, Cota

class pedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ('custo','estado','coment','produto')

class cotaForm(ModelForm):
    class Meta:
        model = Cota
        fields = ('pedido','comanda')
