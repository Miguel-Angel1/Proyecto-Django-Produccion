"""
Sección 5: Vistas en Django
#5.2 Vistas Basadas en Clases – Aplicación Home_Pruebas.
#5.2.3 Importamos las vistas
"""
from django.urls import path

from . import views

urlpatterns = [
    # 5.2.4 Creamos la url que nos llevara a la vista PruebaView
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaList.as_view()),
    # 5.7 Vistas genéricas y modelos – conceptos Básicos – Aplicación Home_Pruebas
    # 5.7.3: url de la viewlist ListarPrueba
    path('registros/', views.ListarPrueba.as_view()),
    path('form/', views.PruebaCreateView.as_view(), name="prueba_add"),
    path('grillas/', views.Grillas.as_view(), name="foundation"),
    path('Practica1/', views.Practica1.as_view(), name="foundation"),

]
