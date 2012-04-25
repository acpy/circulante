# coding: utf-8

from .models import Publicacao

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .isbn import validatedISBN10

from .forms import PublicacaoModelForm

def busca(request):
    erros = []
    pubs = None
    q = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            erros.append(u'Digite um termo para a busca.')
        elif len(q) > 20:
            erros.append(u'Digite no máximo 20 caracteres.')
        else:
            isbn = validatedISBN10(q)
            if isbn:
                pubs = Publicacao.objects.filter(id_padrao=isbn)
            else:    
                pubs = Publicacao.objects.filter(titulo__icontains=q)
    vars_template = {'erros': erros, 'q': q}
    if pubs is not None:
        vars_template['publicacao'] = pubs
        vars_template['pesquisa'] = True
    return render(request, 'catalogo/busca.html', vars_template)

def catalogar(request):
    if request.method != 'POST':
        formulario = PublicacaoModelForm()         
    else:
        formulario = PublicacaoModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            titulo = formulario.cleaned_data['titulo']
            return HttpResponseRedirect(reverse('busca')+'?q='+titulo)   
    return render(request, 'catalogo/catalogar.html',
        {'formulario':formulario})    




