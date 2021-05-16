from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .forms import ContatoPFForm
from .models import ContatoPF

# Create your views here.
def ContatoLista(request):
    contatos = ContatoPF.objects.filter(ativo=True)
    return render(request,
                  'contatopf/lista.html', {'contatos': contatos})

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