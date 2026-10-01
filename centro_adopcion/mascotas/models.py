from django.db import models

# Create your models here.from django.db import models

from django.db import models

class Mascota(models.Model):
    ESTADOS = [
        ('proceso', 'En proceso de adopción'),
        ('adoptado', 'Adoptado'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)  # perro, gato, etc.
    edad = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='proceso')

    def __str__(self):
        return f"{self.nombre} ({self.get_estado_display()})"

