from django import forms

class FormularioEstudio(forms.ModelForm):
    
    universidad = forms.CharField()
    titulo = forms.CharField()
    duracion = forms.IntegerField()
    familiar = forms.CharField()    