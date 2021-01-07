from django.contrib import admin

# 5.6 Models para vistas en Django - Aplicación Home_Pruebas
# 5.6.1: Registro de nuestro modelo en el admin de django
# Importamos el modelo Prueba y depues en el admin.site lo registramos, de esta manera
# ya podremos ver nuestro modelo en el admin de django
from .models import Prueba

# Register your models here.

admin.site.register(Prueba)
