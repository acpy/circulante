from django.conf.urls import patterns, include, url

from .views import busca, catalogar

urlpatterns = patterns('',
    url(r'busca', busca, name='busca'),
    url(r'catalogar', catalogar),
)
