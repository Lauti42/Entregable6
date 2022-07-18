from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

from app_Familia.models import Familiar

# Create your views here.

def familiar(self, nombre, apellido, edad, parentesco):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, parentesco=parentesco)
    familiar.save()

    return HttpResponse(f"""
        <p>Se genero el familiar: {familiar.nombre} {familiar.apellido}</p>
    """)

def VistaFamiliares(self):

    plantilla = loader.get_template("templatefamilia.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)

def VistaParentesco(self):

    plantilla = loader.get_template("templateparentesco.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)

def VistaMenoresymayores(self):

    plantilla = loader.get_template("templatemenorymayor.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)