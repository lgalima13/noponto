from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .forms import ContatoPFForm
from .models import ContatoPF, Promotor

# Create your views here.
def ContatoLista(request):
    contatos = ContatoPF.objects.filter(ativo=True)
    return render(request,
                  'contatopf/lista.html', {'contatos': contatos})

def ContatoCadastro(request):
    contatos = ContatoPF.objects.all()
    if request.method == 'POST':
        form = ContatoPFForm(request.POST)
        if form.is_valid():
            contatos = form.save(commit=False)
            contatos.save()
            return redirect('/contatopf/')
    else:
        form = ContatoPFForm
    return render(request,
                  'contatopf/cadastro.html', {'contatos': contatos,
                                              'form': form})

def ContatoDetalhe(request, id):
    contato = get_object_or_404(ContatoPF, pk=id)
    form = ContatoPFForm(instance=contato)
    return render(request,
                  'contatopf/detalhe.html', {'contato': contato,
                                             'form': form})

def ContatoEditar(request, id):
    contato = get_object_or_404(ContatoPF, pk=id)
    form = ContatoPFForm(instance=contato)
    if(request.method == 'POST'):
        form = ContatoPFForm(request.POST, instance=contato)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('ContatoDetalhe', args=[contato.id]))
        else:
            return render(request, 'contatopf/editar.html', {'contato': contato,
                                                        'form': form})
    else:
        return render(request, 'contatopf/editar.html', {'contato': contato,
                                                    'form': form})
    return render(request,
                  'contatopf/editar.html', {'contato': contato,
                                            'form': form})

def PromotorLista(request):
    promotores = Promotor.objects.all()
    return render(request,
                  'motorista/lista.html', {'promotores': promotores})


