from django.urls import path

from .views import amigos, buscar, estudios, familia, inicio, trabajos, nuevofamiliar, VistaParentesco, VistaMenoresymayores, formulariofamilia, busquedaFamiliar, buscar


urlpatterns = [
    path('agregar-familiar/<nombre>/<apellido>/<edad>/<parentesco>', nuevofamiliar),    
    path('familia/parentesco/', VistaParentesco, name='Parentesco'),
    path('familia/menores-y-mayores/', VistaMenoresymayores, name='Menor-y-mayor'),
    path('', inicio, name="Inicio"),
    path('familiares/', familia, name="Familia"),
    path('amigos/', amigos, name="Amigos"),
    path('estudios/',estudios, name="Estudios"),
    path('trabajos/', trabajos, name="Trabajos"),
    path('busqueda-familiar/', busquedaFamiliar, name="Busqueda"),
    path('buscar/', buscar, name="Buscar"),
    path('formulario-familia/', formulariofamilia, name="Formulario"),

]
