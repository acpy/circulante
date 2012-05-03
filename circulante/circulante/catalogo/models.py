# coding: utf-8

from django.db import models

TIPOS_PUBLICACAO = (
    (u'livro', u'livro'),
    (u'apostila', u'apostila'),
    (u'gibi', u'gibi'),
    (u'outro', u'outro'),
)

class Publicacao(models.Model):
    tipo = models.CharField(max_length=16, choices=TIPOS_PUBLICACAO,
                            default=TIPOS_PUBLICACAO[0][0])
    id_padrao = models.CharField(max_length=32, blank=True)
    titulo = models.CharField(max_length=256)
    num_paginas = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = u'Publicação'
        verbose_name_plural = u'Publicações'
    
    def __unicode__(self):
        return self.titulo
    

class Credito(models.Model):
    nome = models.CharField(max_length=256)
    papel = models.CharField(max_length=32, blank=True)
    publicacao = models.ForeignKey(Publicacao)
    
    def __unicode__(self):
        return self.nome
    
    
