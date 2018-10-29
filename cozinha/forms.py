from django.forms import ModelForm
from .models import Aux_form

class aux_Form(ModelForm):
    class Meta:
        model =  Aux_form
        fields = ('IDaux','transicao')
