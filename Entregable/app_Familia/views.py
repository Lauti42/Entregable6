from django.http import HttpResponse
from django.shortcuts import render

from app_Familia.models import Familiar

# Create your views here.

def familiar(self, nombre, apellido, edad, parentesco):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, parentesco=parentesco)
    familiar.save()

    return HttpResponse(f"""
        <p>Se genero el familiar: {familiar.nombre} {familiar.apellido}</p>
    """)