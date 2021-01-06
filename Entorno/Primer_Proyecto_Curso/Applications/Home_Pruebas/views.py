# 5.7 Vistas genéricas y modelos – conceptos Básicos – Aplicación Home_Pruebas
# 5.7.2: Importamos nuestro modelo para poder trabajar con el en la seccion 5.7.1
# Sección 5: Vistas en Django
# 5.2 Vistas Basadas en Clases – Aplicación Home_Pruebas.
# Importamos el modulo de django para trabajar con las vistas genericas
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView)

# 9.2 Model Form Parte 1
# Importamos el formulario con el cual trabajaremos
from .forms import PruebaForm
from .models import Prueba


# Sección 5: Vistas en Django
# 5.5 Conociendo mas de las vistas genéricas - Aplicación Home_Pruebas.º
# Creación de una clase para ListView, debemos importar el modulp ListView
class PruebaList(ListView):
    template_name = 'Templates_Home_Pruebas/listar.html'
    context_object_name = 'listanum'
    queryset = ['1', '2', '3']


# 5.2.1 Creamos la clase y le indicamos con que template queremos trabajar,
# en este caso sera prueba.html.
class PruebaView(TemplateView):
    template_name = 'Templates_Home_Pruebas/prueba.html'


class Practica1(TemplateView):
    template_name = 'Templates_Home_Pruebas/Practica1.html'


# 10.5 Sistema Grillas Foundation Teoría.
class Grillas(TemplateView):
    template_name = 'Templates_Home_Pruebas/grillas.html'


# 5.7 Vistas genéricas y modelos – conceptos Básicos – Aplicación Home_Pruebas
# Vamos a crear un Listview, el cual listara nuestro registro de nuestro modelo Prueba, creado en la seccion 5.6
class ListarPrueba(ListView):
    template_name = 'Templates_Home_Pruebas/listar_prueba.html'

    # 5.7 Vistas genéricas y modelos – conceptos Básicos – Aplicación Home_Pruebas
    # 5.7.1: Elegimos el modelo con el cual vamos a trabajar, en este caso sera prueba,
    # pero debemos importar primero nuestro modelo, 5.7.2 . . . >
    # Ya que importamos nuestro modelo ahora si vamos a poder trabajar con el.
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = 'Templates_Home_Pruebas/adda.html'
    model = Prueba
    # 9.2 Model Form Parte 1
    # Mandamos llamar al formulario
    form_class = PruebaForm
    success_url = "/"
