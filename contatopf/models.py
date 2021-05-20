from django.db import models

class PreCadastro(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    email = models.EmailField()
    ativo = models.BooleanField(default=True)
    objects = models.Manager()


    def __str__(self):
        return self.nome

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
    precadastro = models.OneToOneField(PreCadastro,
                                    on_delete = models.CASCADE,
                                    primary_key = True)
    datanascimento = models.DateField()
    datacadastro = models.DateTimeField(auto_now=True)
    sexo = models.CharField(max_length=10,
                            choices=SEXO_CHOICES,
                            default='feminino')
    rg = models.CharField(max_length=12, blank=True)
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

    def __int__(self):
        return self.precadastro

class Promotor(models.Model):
    precadastro = models.ForeignKey(PreCadastro,
                                  verbose_name='Promotor_PreCadastro',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    altura = models.IntegerField(blank=True)
    manequim = models.IntegerField(blank=True)
    calcado = models.IntegerField(blank=True)
    objects = models.Manager()
    def __int__(self):
        return self.precadastro

class Motorista(models.Model):
    CATEGORIA_CHOICES = (
        ('categoriaa', 'Categoria A'),
        ('categoriab', 'Categoria B'),
        ('categoriac', 'Categoria C'),
        ('categoriae', 'Categoria E'),
    )
    precadastro = models.ForeignKey(PreCadastro,
                                  verbose_name='Motorista_PreCadastro',
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

    def __int__(self):
        return self.precadastro

class Reporter(models.Model):
    precadastro = models.ForeignKey(PreCadastro,
                                  verbose_name='Reporter_PreCadastro',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True)
    access = models.BooleanField(default=False)
    irig = models.BooleanField(default=False)

    def __int__(self):
        return self.precadastro

class Evento(models.Model):
    precadastro = models.ManyToManyField(PreCadastro,
                                  blank=True)
    nome = models.CharField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.nome