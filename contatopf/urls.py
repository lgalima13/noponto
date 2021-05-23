from . import views
from django.urls import path

urlpatterns = [
    path('', views.EventoLista, name='EventoLista'),
    path('eventodetalhe/<int:id>', views.EventoDetalhe, name='EventoDetalhe'),
    path('dataeventolista/', views.DataEventoLista, name='dataeventolista'),
    path('dataeventodetalhe/<int:id>', views.DataEventoDetalhe, name='dataeventodetalhe'),
    path('precadastrolista/', views.PreCadastroLista, name='precadastrolista'),
    path('contatolista/', views.ContatoLista, name='ContatoLista'),
    path('contatodetalhe/<int:id>', views.ContatoDetalhe, name='ContatoDetalhe'),
    path('contatoeditar/<int:id>', views.ContatoEditar, name='ContatoEditar'),
    path('contatocadastro/', views.ContatoCadastro, name='ContatoCadastro'),
    path('promotorlista/', views.PromotorLista, name='PromotorLista'),
    path('promotorcadastro/', views.PromotorCadastro, name='PromotorCadastro'),
    path('motoristalista/', views.MotoristaLista, name='MotoristaLista'),
    path('motoristacadastro/', views.MotoristaCadastro, name='MotoristaCadastro')
]