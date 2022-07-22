from django import forms

class FormularioFamilia(forms.Form):


    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    parentesco = forms.CharField()    