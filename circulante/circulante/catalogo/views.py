# coding: utf-8

from .models import Publicacao, Credito

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.utils.http import urlquote

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
        #elif len(q) > 80:
        #    erros.append(u'Digite no máximo 80 caracteres.')
        else:
            isbn = validatedISBN10(q)
            if isbn:
                pubs = Publicacao.objects.filter(id_padrao=isbn)
            else:    
                pubs = Publicacao.objects.filter(titulo__icontains=q)
    vars_template = {'erros': erros, 'q': q}
    if pubs is not None:
        vars_template['publicacoes'] = pubs
        vars_template['pesquisa'] = True
    return render(request, 'catalogo/busca.html', vars_template)

def catalogar(request):
    CreditoInlineFormSet = inlineformset_factory(Publicacao, Credito)
    if request.method == 'POST':
        formulario = PublicacaoModelForm(request.POST)
        if formulario.is_valid():
            pub = formulario.save()
            formset = CreditoInlineFormSet(request.POST, instance=pub)        
            formset.save()
            titulo = formulario.cleaned_data['titulo']
            return HttpResponseRedirect(reverse('busca')+'?q='+urlquote(titulo))   
    else:
        formulario = PublicacaoModelForm()
        formset = CreditoInlineFormSet()        
    return render(request, 'catalogo/catalogar.html',
        {'formulario':formulario, 
         'formset':formset})    

def editar(request, pk):
    pub = get_object_or_404(Publicacao, pk=pk)
    CreditoInlineFormSet = inlineformset_factory(Publicacao, Credito)
    if request.method == 'POST':
        formulario = PublicacaoModelForm(request.POST, instance=pub)
        formset = CreditoInlineFormSet(request.POST, instance=pub)        
        if formulario.is_valid() and formset.is_valid():
            formulario.save()
            formset.save()
            titulo = formulario.cleaned_data['titulo']
            return HttpResponseRedirect(reverse('busca')+'?q='+urlquote(titulo))
    else:
        formulario = PublicacaoModelForm(instance=pub)
        formset = CreditoInlineFormSet(instance=pub)        
    return render(request, 'catalogo/catalogar.html',
        {'formulario':formulario, 
         'formset':formset})    










