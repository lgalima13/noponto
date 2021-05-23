from django import forms
from .models import ContatoPF, Motorista, Promotor, Reporter, Evento, PreCadastro, DataEvento

class PreCadastroForm(forms.ModelForm):
    nome = forms.CharField(label='Nome Completo', widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    cpf = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))

    class Meta:
        model = PreCadastro
        fields = ['nome', 'cpf', 'email']

class ContatoPFForm(forms.ModelForm):
    precadastro = forms.SelectMultiple(attrs={'class': 'form-control', 'required': 'false'})
    datanascimento = forms.DateField(required=False, widget=forms.widgets.DateInput(format="%d/%m/%Y"), label='Data Nascimento')
    sexo = forms.SelectMultiple(attrs={'class': 'form-control', 'required': 'false'})
    rg = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    endereco = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    bairro = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}) )
    cidade = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    cep = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    fone1 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    fone2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    contatoemergencia = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    fone3 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    fone4 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    parentesco = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    instagram = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    escolaridade = forms.SelectMultiple(attrs={'class': 'form-control', 'required': 'false'})
    faculdade = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    disponibilidade = forms.SelectMultiple(attrs={'class': 'form-control', 'required': 'false'})
    autorizacao = forms.BooleanField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    ativo = forms.BooleanField(required=False)

    class Meta:
        model = ContatoPF
        fields = ['precadastro', 'datanascimento', 'sexo', 'rg', 'endereco', 'bairro', 'cidade', 'cep',
                  'fone1', 'fone2', 'fone3', 'fone4','contatoemergencia', 'parentesco', 'instagram', 'escolaridade',
                  'faculdade', 'disponibilidade', 'autorizacao', 'ativo']

class PromotorForm(forms.ModelForm):
    precadastro = forms.SelectMultiple()
    altura = forms.IntegerField(required=False)
    manequim = forms.IntegerField(required=False)
    calcado = forms.IntegerField(required=False)

    class Meta:
        model = Promotor
        fields = ['precadastro', 'altura', 'manequim', 'calcado']

class MotoristaForm(forms.ModelForm):
    precadastro = forms.SelectMultiple()
    categoria = forms.SelectMultiple()
    datahabilitacao = forms.DateField()
    validadehabilitacao = forms.DateField()

    class Meta:
        model = Motorista
        fields = ['precadastro', 'categoria', 'datahabilitacao', 'validadehabilitacao']

class EventoForm(forms.ModelForm):
    precadastro = forms.SelectMultiple()
    nome = forms.CharField()

    class Meta:
        model = Evento
        fields = ['precadastro', 'nome']

class DataEventoForm(forms.ModelForm):
    evento = forms.SelectMultiple()
    dataevento = forms.DateField(required=False, widget=forms.widgets.DateInput(format="%d/%m/%Y"), label='Data')
    confirmado = forms.BooleanField(required=False)
    endereco = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    bairro = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    cidade = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    cep = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))
    observacoes = forms.CharField(label='Observações',required=False, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':4, 'cols':40}))

    class Meta:
        model = DataEvento
        fields = ['evento', 'dataevento', 'confirmado', 'endereco', 'bairro', 'cidade', 'cep', 'observacoes']
