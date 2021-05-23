from django.contrib import admin
from .models import ContatoPF, Promotor, Motorista, Reporter, Evento, PreCadastro, DataEvento

admin.site.register(PreCadastro)
admin.site.register(ContatoPF)
admin.site.register(Promotor)
admin.site.register(Motorista)
admin.site.register(Reporter)
admin.site.register(Evento)
admin.site.register(DataEvento)