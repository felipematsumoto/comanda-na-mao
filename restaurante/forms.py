from django.forms import ModelForm

from .models import Restaurante

class restauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ('nome','cnpj','nomeDono','telefone','endereco','foto', 'email','dono')
