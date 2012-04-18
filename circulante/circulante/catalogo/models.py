# coding: utf-8

from django.db import models

TIPOS_PUBLICACAO = (
    (u'livro', u'Livro'),
    (u'apostila', u'Apostila'),
    (u'gibi', u'Gibi'),
)

class Publicacao(models.Model):
    tipo = models.CharField(max_length=16, choices=TIPOS_PUBLICACAO,
                            default=TIPOS_PUBLICACAO[0][0])
    id_padrao = models.CharField(max_length=32, blank=True)
    titulo = models.CharField(max_length=256)
    
