from django.urls import path

from . import views

# 8.1 ListView – Documentación
# 8.1.2 importamos el modulo para las vistas y cremos la url

# 9.2 Redirección dentro de un CreateView – URL Name
# Creacion de etiquetas app_name y name para poder acceder mediante el reverse_lazy

app_name = "empleado_app"

urlpatterns = [
    # Sección 11
    # 11.1 Esquema de las carpetas Templates
    # URL para la vista de inicio
    path('', views.InicioView.as_view(), name='inicio'),

    path('listar_empleados/', views.ListaAllEmpleados.as_view(), name='listar_all_empleados'),
    path('listar_departamento/', views.ListByArea.as_view()),
    # Sección 8: Vista en django
    # 8.3 Parámetro por URL y filtro ListView
    # Envio de la variable a la vista.
    path('lista_function/<variable>/', views.ListByAreaFunction.as_view(), name='lista_area'),
    path('busqueda-empleado/', views.ListaEmpleadoByKeybor.as_view()),
    path('habilidades/', views.ListarHabilidadesEmpleado.as_view()),
    path('Detailview/<pk>/', views.DetallaDeListaCompleta.as_view(), name='lista_detallada'),
    path('Registro/', views.EmpleadoCreateView.as_view(), name='registro_empleado'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
    path('listarAdmin/', views.ListaEmpleadosAdmin.as_view(), name='listar_empleados_administrador'),
]
