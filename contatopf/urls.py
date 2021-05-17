from . import views
from django.urls import path

urlpatterns = [
    path('', views.ContatoLista, name='ContatoLista'),
    path('contatodetalhe/<int:id>', views.ContatoDetalhe, name='ContatoDetalhe'),
    path('contatoeditar/<int:id>', views.ContatoEditar, name='ContatoEditar'),
    path('contatocadastro/', views.ContatoCadastro, name='ContatoCadastro'),
    path('promotorlista/', views.PromotorLista, name='PromotorLista'),
    path('promotorcadastro/', views.PromotorCadastro, name='PromotorCadastro')
]