"""
Sección 4:Sección 4: Entorno de trabajo optimo en Django
4.5 Urls de aplicaciones
"""
from django.urls import path

from . import views

app_name = "departamento_app"

urlpatterns = [
    path('listaDepartamento/', views.ListarDepartamento.as_view(), name="listar"),
    path('new-depa/', views.NewDepartamento.as_view(), name="nuevo_departamento"),
]
