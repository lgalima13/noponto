from django.db import models


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
    nome = models.CharField(max_length=150, null=False)
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
    fone1 = models.CharField(max_length=20, blank=True)
    fone2 = models.CharField(max_length=20, blank=True)
    fone3 = models.CharField(max_length=20, blank=True)
    fone4 = models.CharField(max_length=20, blank=True)
    contatoemergencia = models.CharField(max_length=150, null=False)
    parentesco = models.CharField(max_length=50, null=False)
    email = models.EmailField(blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    altura = models.IntegerField(blank=True)
    manequim = models.IntegerField(blank=True)
    calcado = models.IntegerField(blank=True)
    escolaridade = models.CharField(max_length=6,
                                    choices=ESCOLARIDADE_CHOICES,
                                    default='fundai')
    faculdade = models.CharField(max_length=150, blank=True)



