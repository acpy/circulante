# coding: utf-8

from django.forms import ModelForm

from .models import Publicacao

class PublicacaoModelForm(ModelForm):
    class Meta:
        model = Publicacao

