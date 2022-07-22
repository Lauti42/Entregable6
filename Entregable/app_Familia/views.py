from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from app_Familia.forms import FormularioFamilia

from app_Familia.models import Familiar

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


    # print('method', request.method)
    # print('post', request.POST)

    # if request.method == 'POST':

    #     familiar = Familiar( nombre=request.POST['nombre'], apellido=request.POST['apellido'], edad=request.POST['edad'], parentesco=request.POST['parentesco'])
        
    #     familiar.save()

    #     return render(request, 'inicio.html')

    # return render(request, 'formulario-familia.html')

    print('method', request.method)
    print('post', request.POST)

    if request.method == 'POST':

        miformulario = FormularioFamilia(request.POST)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            familiar = Familiar( nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'], parentesco=data['parentesco'])
        
            familiar.save()

            return render(request, 'inicio.html')

    else:
        
        miformulario = FormularioFamilia() 

    return render(request, 'formulario-familia.html', {'miformulario': miformulario})

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