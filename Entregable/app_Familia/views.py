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

    plantilla = loader.get_template("familia.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)

def VistaParentesco(self):

    plantilla = loader.get_template("parentesco.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)

def VistaMenoresymayores(self):

    plantilla = loader.get_template("menor-y-mayor.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)

def inicio(self):

    return render(self, "inicio.html")

def familia(self):

    return render(self, "familiares.html")

def amigos(self):

    return render(self, "amigos.html")

def estudios(self):

    return render(self, "estudios.html")

def trabajos(self):

    return render(self, "trabajos.html")

