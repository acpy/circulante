# coding: utf-8

from django.contrib import admin
from .models import Publicacao, Credito

#class CreditoInline(admin.StackedInline):
#    model = Credito

class CreditoInline(admin.TabularInline):
    model = Credito

class PublicacaoAdmin(admin.ModelAdmin):
    inlines = [CreditoInline]

admin.site.register(Publicacao, PublicacaoAdmin)
