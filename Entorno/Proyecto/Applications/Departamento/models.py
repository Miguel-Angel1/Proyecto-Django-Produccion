from django.db import models


# Create your models here.


# Sección 6: Bases de Datos en Django – Models.py
# 6.2 Tipos de Campos de un Modelo
class Departamento(models.Model):
    # 'Nombre' es solo representativo y es la forma en como se vera en el admin de django.
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('Anulado', default=False)

    # 7.0 Administrador de Django
    # 7.1 Class Meta, modelos y el Administrador de Django.
    # Podemos cambiar el nombre representativo del modelo
    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.short_name
    # return str(self.id) + '-' + self.name + '-' + self.short_name
    # Para int str
