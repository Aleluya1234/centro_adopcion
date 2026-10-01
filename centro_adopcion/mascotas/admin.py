from django.contrib import admin
from .models import Mascota

# Register your models here.

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'edad', 'estado')
    list_filter = ('estado', 'especie')

