from django.db import models
from django.db.models import Q

#Managers

class AutorManager(models.Manager):
    """Manager para el modelo Autor"""
    
    def buscar_autor(self,kword):
        """Filtrar entre un resultado U otro"""
        
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
            )
        
        return resultado
    
    def buscar_autor2(self,kword):
        """excluir en una busqueda"""
        resultado = self.filter(
            nombre__icontains=kword
            ).exclude(
        #"""tambien se pueden hacer filtros de filtros, en vez de .exclude podemos agregar otro .filter""" 
                Q(edad__icontains=35) | Q(apellidos__icontains=65)
            )
        
        return resultado
    
    
    def buscar_autor3(self,kword):
        """Filtrar por un resultado Y otro (mayor o menor)"""
        resultado = self.filter(
            edad__gt = 35,
            edad__lt = 65
            ).order_by('apellidos','nombre')
    
        return resultado 