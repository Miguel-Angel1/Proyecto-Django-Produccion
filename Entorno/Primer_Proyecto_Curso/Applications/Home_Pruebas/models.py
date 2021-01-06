from django.db import models


# Create your models here.

# 5.6 Models para vistas en Django - Aplicación Home_Pruebas
# Creación de modelos en django.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + "  " + self.subtitulo
