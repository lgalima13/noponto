from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .forms import ContatoPFForm, PromotorForm, MotoristaForm, EventoForm, PreCadastroForm
from .models import ContatoPF, Promotor, Motorista, Evento, PreCadastro

# Create your views here.

def PreCadastroLista(request):
    precadastros = PreCadastro.objects.filter(ativo=True)
    return render(request,
                  'precadastro/lista.html', {'precadastros': precadastros})

def PreCadastroCadastro(request):
    precadastro = PreCadastro.objects.all()
    if request.method == 'POST':
        form = PreCadastroForm(request.POST)
        if form.is_valid():
            precadastro = form.save(commit=False)
            precadastro.save()
            return  redirect('/precadastro/')
    else:
        form = PreCadastroForm
    return render(request,
                  'precadastro/cadastro.html', {'precadastro': precadastro,
                                                'form': form})


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
    promotores = Promotor.objects.filter(precadastro=id)
    motoristas = Motorista.objects.filter(precadastro=id)
    form = ContatoPFForm(instance=contato)
    return render(request,
                  'contatopf/detalhe.html', {'contato': contato,
                                             'promotores': promotores,
                                             'motoristas': motoristas,
                                             'form': form})

def EventoDetalhe(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(instance=evento)
    return render(request,
                  'evento/detalhe.html', {'evento': evento,
                                          'form': form})

def EventoLista(request):
    eventos = Evento.objects.all()
    return render(request,
                  'evento/lista.html', {'eventos': eventos})


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
                  'promotor/lista.html', {'promotores': promotores})

def PromotorCadastro(request):
    promotores = Promotor.objects.all()
    if request.method == 'POST':
        form = PromotorForm(request.POST)
        if form.is_valid():
            promotores = form.save(commit=False)
            promotores.save()
            return redirect('/promotorlista/')
    else:
        form = PromotorForm
    return render(request,
                  'promotor/cadastro.html', {'promotores': promotores,
                                                       'form': form})

def MotoristaCadastro(request):
    motoristas = Motorista.objects.all()
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            motoristas = form.save(commit=False)
            motoristas.save()
            return redirect('/motoristalista/')
    else:
        form = MotoristaForm
    return render(request,
                  'motorista/cadastro.html', {'motoristas': motoristas,
                                              'form': form})

def MotoristaLista(request):
    motoristas = Motorista.objects.all()
    return render(request,
                  'motorista/lista.html', {'motoristas': motoristas})




