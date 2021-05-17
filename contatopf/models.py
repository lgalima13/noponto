from django.db import models
from datetime import datetime

class ContatoPF(models.Model):
    SEXO_CHOICES = (
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
        ('indefinido', 'Indefinido'),
    )
    ESCOLARIDADE_CHOICES = (
        ('fundai', 'Fundamental Incompleto'),
        ('fundac', 'Fundamental Completo'),
        ('medioi', 'Ensino Médio Completo'),
        ('medioc', 'Ensino Médio Incompleto'),
        ('superi', 'Superior Incompleto'),
        ('superc', 'Superior Completo'),
        ('posgra', 'Pós-Graduação'),
    )
    DISPONIBILIDADE_CHOICES = (
        ('manha', 'Horário Manhã'),
        ('tarde', 'Horário Tarde'),
        ('noite', 'Horário Noite'),
        ('final', 'Final de Semana'),
        ('flexi', 'Flexível'),
    )
    nome = models.CharField(max_length=150, null=False, verbose_name='Nome Completo')
    datanascimento = models.DateField()
    datacadastro = models.DateTimeField(auto_now=True)
    sexo = models.CharField(max_length=10,
                            choices=SEXO_CHOICES,
                            default='feminino')
    rg = models.CharField(max_length=12, blank=True)
    cpf = models.CharField(max_length=12, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=150, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    fone1 = models.CharField(max_length=20, blank=True, null=True)
    fone2 = models.CharField(max_length=20, blank=True, null=True)
    fone3 = models.CharField(max_length=20, blank=True, null=True)
    fone4 = models.CharField(max_length=20, blank=True, null=True)
    contatoemergencia = models.CharField(max_length=150, null=False)
    parentesco = models.CharField(max_length=50, null=False)
    email = models.EmailField(blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    escolaridade = models.CharField(max_length=6,
                                    choices=ESCOLARIDADE_CHOICES,
                                    default='fundai')
    faculdade = models.CharField(max_length=150, blank=True)
    disponibilidade = models.CharField(max_length=5,
                                       choices=DISPONIBILIDADE_CHOICES,
                                       default='flexi')
    autorizacao = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return self.nome

class Promotor(models.Model):
    contatopf = models.ForeignKey(ContatoPF,
                                  verbose_name='Promotor_ContatoPF',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    altura = models.IntegerField(blank=True)
    manequim = models.IntegerField(blank=True)
    calcado = models.IntegerField(blank=True)
    objects = models.Manager()

class Motorista(models.Model):
    CATEGORIA_CHOICES = (
        ('categoriaa', 'Categoria A'),
        ('categoriab', 'Categoria B'),
        ('categoriac', 'Categoria C'),
        ('categoriae', 'Categoria E'),
    )
    contatopf = models.ForeignKey(ContatoPF,
                                  verbose_name='Motorista_ContatoPF',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    categoria = models.CharField(
        max_length=10,
        choices=CATEGORIA_CHOICES,
        default='categoriab'
    )
    datahabilitacao = models.DateField()
    validadehabilitacao = models.DateField()

class Reporter(models.Model):
    contatopf = models.ForeignKey(ContatoPF,
                                  verbose_name='Reporter_ContatoPF',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    access = models.BooleanField(default=False)
    irig = models.BooleanField(default=False)

