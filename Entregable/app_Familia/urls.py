from django.urls import path
from app_Familia.views import amigos, estudios, familia, inicio, trabajos, familiar, VistaFamiliares, VistaParentesco, VistaMenoresymayores


urlpatterns = [
    path('familia/', VistaFamiliares),
    path('familia/parentesco/', VistaParentesco),
    path('familia/menores-y-mayores/', VistaMenoresymayores),
    path('agregar-familiar/<nombre>/<apellido>/<edad>/<parentesco>', familiar),
    path('', inicio),
    path('familiares/', familia),
    path('amigos/', amigos),
    path('estudios/',estudios),
    path('trabajos/', trabajos),

]
