
from django.template import Context, Template, loader
from django.http import HttpResponse

def VistaFamiliares(request):
    plantilla = loader.get_template("templatefamilia.html")

    documento = plantilla.render()

    return HttpResponse(documento)