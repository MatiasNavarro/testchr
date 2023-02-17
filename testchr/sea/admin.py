from django.contrib import admin

from .models import Proyecto

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ("id", "nombre", "tipo", "region", "topologia", "titular", "inversion", "fecha_presentacion_ingreso", "estado", "mapa")

admin.site.register(Proyecto, ProyectoAdmin)