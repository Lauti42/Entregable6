from django.contrib import admin
from .models import Amigos, Estudios, Familiar, Trabajos

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad', 'parentesco']
    search_fields = ['nombre', 'apellido']

# Register your models here.
admin.site.register(Familiar, FamiliaAdmin)
admin.site.register(Estudios)
admin.site.register(Amigos)
admin.site.register(Trabajos)
