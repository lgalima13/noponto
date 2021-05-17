from django import forms
from .models import ContatoPF, Motorista, Promotor, Reporter

class ContatoPFForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    datanascimento = forms.DateField(required=False)
    sexo = forms.SelectMultiple()
    rg = forms.CharField(required=False)
    cpf = forms.CharField(required=False)
    endereco = forms.CharField(required=False)
    bairro = forms.CharField(required=False)
    cidade = forms.CharField(required=False)
    cep = forms.CharField(required=False)
    fone1 = forms.CharField(required=False)
    fone2 = forms.CharField(required=False)
    contatoemergencia = forms.CharField()
    fone3 = forms.CharField(required=False)
    fone4 = forms.CharField(required=False)
    parentesco = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    instagram = forms.CharField(required=False)
    escolaridade = forms.SelectMultiple()
    faculdade = forms.CharField(required=False)
    disponibilidade = forms.SelectMultiple()
    autorizacao = forms.BooleanField(required=False)
    ativo = forms.BooleanField(required=False)

    class Meta:
        model = ContatoPF
        fields = ['nome', 'datanascimento', 'sexo', 'rg', 'cpf', 'endereco', 'bairro', 'cidade', 'cep',
                  'fone1', 'fone2', 'fone3', 'fone4','contatoemergencia', 'parentesco', 'email', 'instagram', 'escolaridade',
                  'faculdade', 'disponibilidade', 'autorizacao', 'ativo']

