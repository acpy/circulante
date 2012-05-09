from django.conf.urls import patterns, include, url

from .views import busca, catalogar, editar

urlpatterns = patterns('',
    url(r'catalogar', catalogar, name='catalogar'),
    url(r'editar/(\d+)', editar, name='editar'),
    url(r'', busca, name='busca'),
)
