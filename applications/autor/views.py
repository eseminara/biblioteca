from django.shortcuts import render
from django.views.generic import ListView

# Models Local
from .models import Autor
# Create your views here.


class ListaAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista_autores.html'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        return Autor.objects.buscar_autor3(palabra_clave)
