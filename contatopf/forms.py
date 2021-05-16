from django import forms
from .models import ContatoPF, Motorista, Promotor, Reporter

class ContatoPFForm(forms.ModelForm):
    nome = forms.CharField()
    sexo = forms.SelectMultiple()

    class Meta:
        model = ContatoPF
        fields = ['nome', 'sexo']
