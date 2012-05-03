# coding: utf-8

from django.forms import ModelForm, ValidationError

from .models import Publicacao

from .isbn import validatedISBN10

class PublicacaoModelForm(ModelForm):
    class Meta:
        model = Publicacao
    
    def clean_id_padrao(self):
        dado = self.cleaned_data['id_padrao']
        if self.cleaned_data['tipo'] == 'livro':
            isbn = validatedISBN10(dado)
            if isbn:
                pass
                #dado = isbn # para salvar sem hifens
            else:
                msg = u'Para livros, o id_padrao deve ser um ISBN válido'
                raise ValidationError(msg)
        return dado
        

