from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
        
class Amigos(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    amigodesde = models.IntegerField()

class Estudios(models.Model):
    profesor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()

class Trabajos(models.Model):
    empresa = models.CharField(max_length=50)
    tiempo = models.IntegerField()

