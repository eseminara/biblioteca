from django.contrib import admin
from django.urls import path

#Views
from .views import ListaAutores

urlpatterns = [
    path(
        'lista_autores/',
        ListaAutores.as_view(), 
        name='autores'
        ),
    
]