from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    topologia = models.CharField(max_length=255)
    titular = models.CharField(max_length=255)
    inversion = models.DecimalField(max_digits=10, decimal_places=4)
    fecha_presentacion_ingreso = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    mapa = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.nombre}"