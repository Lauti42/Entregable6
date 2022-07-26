
from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.parentesco}'

    class Meta():
        verbose_name = 'family'
        verbose_name_plural = 'My familys'
        ordering = ('nombre', '-edad')
        unique_together = ('nombre', 'apellido')
        
class Amigos(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    amigodesde = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}'

class Estudios(models.Model):
    universidad = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    duracion = models.IntegerField()
    familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.titulo} - {self.duracion} años.'

class Trabajos(models.Model):
    empresa = models.CharField(max_length=50)
    tiempo = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.empresa} - {self.tiempo}'
