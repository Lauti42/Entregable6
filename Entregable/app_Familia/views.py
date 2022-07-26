from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
# from app_Familia.forms import FormularioEstudio

from app_Familia.models import Familiar, Estudios

# Create your views here.

def nuevofamiliar(self, nombre, apellido, edad, parentesco):
    
    familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, parentesco=parentesco)
    familiar.save()

    return HttpResponse(f"""
        <p>Se genero el familiar: {familiar.nombre} {familiar.apellido}</p>
    """)

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

    plantilla = loader.get_template("familiares.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)
    

def amigos(self):

    return render(self, "amigos.html")

def estudios(self):

    return render(self, "estudios.html")

def trabajos(self):

    return render(self, "trabajos.html")

def formulariofamilia(request):


    print('method', request.method)
    print('post', request.POST)

    if request.method == 'POST':

        familiar = Estudios( universidad=request.POST['universidad'], titulo=request.POST['titulo'], duracion=request.POST['duracion'], familiar=request.POST['familiar'])
        
        familiar.save()

        return render(request, 'inicio.html')

    plantilla = loader.get_template("formulario-familia.html")

    documento = plantilla.render({"familia": Familiar.objects.all()})

    return HttpResponse(documento)



    # print('method', request.method)
    # print('post', request.POST)

    # if request.method == 'POST':

    #     miformulario = FormularioEstudio(request.POST)

    #     if miformulario.is_valid():

    #         data = miformulario.cleaned_data

    #         estudio = Estudios( universidad=data['universidad'], titulo=data['titulo'], duracion=data['duracion'], familiar=data['familiar'])
        
    #         estudio.save()

    #         return render(request, 'inicio.html')

    # else:
        
    #     miformulario = FormularioEstudio() 

    # return render(request, 'formulario-familia.html', {'miformulario': miformulario})

def busquedaFamiliar(request):  

    return render(request, "busquedaFamiliar.html")

def buscar(request): 

    if request.GET["apellido"]:

        apellido = request.GET["apellido"]

        familiares = Familiar.objects.filter(apellido__icontains=apellido)

        return render (request, "resultadoBusqueda.html", {"familiares": familiares, "apellido": apellido})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)