# Create your views here.

# 9.2 Redirección dentro de un CreateView – URL Name
# Importación del modulo para un mejor manejo de redireciones
from django.urls import reverse_lazy
# Sección 8: Vistas Basadas en Clases
# 8.1 ListView – Documentación
# 8.1.1 importamos el modulo para las vistas
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView)

# 8.1.2 Importamos nuestro modelo: Empleadp
from .models import Empleado
from .forms import EmpleadoForm

# Seccion 11: Desarrollo del primer poryecto del curso
# 11.1 Esquema de la carpeta Templates
# Vista que carga pagina de Inicio
class InicioView(TemplateView):
    template_name = 'inicio.html'


class ListaAllEmpleados(ListView):
    paginate_by = 5
    ordering = 'first_name'
    template_name = 'Templates_Persona/list_all.html'
    context_object_name = 'paginado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
        return lista


# Sección 8: Vistas Basadas en Clases
# 8.2 Filtros en un ListView.
# Creamos una clase para filtrar por areas, mediante filtro, apuntado al campo departamento del modelo Empleado, este campo
# a su vez apunta a una llave foranea hacua el modelo Departamento.

# Hacemos uso del queryset donde indicamos a que modelo hacemos referencia para aplicar el filtro
# y apuntamos al nombre del campo en este caso sera departamento, pero como es llave foranea lo buscamos como short_name
class ListByArea(ListView):
    template_name = 'Templates_Persona/list_area.html'
    queryset = Empleado.objects.filter(
        departamento__short_name='administración'
    )


# -------------------------Listado por Area-------------------------------------------
# Sección 8: Vista en django
# 8.3 Parámetro por URL y filtro ListView
# Haremos uso de  funciones para aplicar filtros
# Como el filtro de identificara por medio de URL, vamos a utilizar el parametro kwargs que hace referencia a lo
# que escribimos en la url, entonces creamos una variable donde guardaremos el valor que se ingrese el la url mediante
# una variable proveniente del arhivo url.py
class ListByAreaFunction(ListView):
    template_name = 'Templates_Persona/list_area.html'
    context_object_name = 'listaAreasEmpleado'

    def get_queryset(self):
        area = self.kwargs['variable']
        lista = Empleado.objects.filter(departamento__short_name=area)
        return lista


# ---------------------------Listado pior palabra------------------------------------------
# Sección 8: Vista en django
# 8.4 Filtrado a través de una caja de texto
# Hacemos uso del metodo self.request para interceptar lo que el usuario ingresa en la caja de texto
# la cual se encuentra en nuestro template, con el id y name kdword, y posterior aplicamos el filtro en lista
class ListaEmpleadoByKeybor(ListView):
    template_name = 'Templates_Persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista


# -------------------------------Manytomany-----------------------------------------
# 8.7 ListView con Relación ManyToMany
class ListarHabilidadesEmpleado(ListView):
    template_name = 'Templates_Persona/habilidades.html'
    context_object_name = 'habilidades'

    # Get recupera un unico registro
    def get_queryset(self):
        empleado = Empleado.objects.get(first_name='LOLA')
        return empleado.habilidades.all()


# ----------------------------------------Listas---------------------------------------------
# 8.8 Vista Genérica DetailView
# Mostrar mas datos de un modelo, mediante el DetailView, para ver mas en detalle los datos de un modelo.
# Debemos importar el detailview en las vistas : Sección 8 vistas basadas en clases.
class DetallaDeListaCompleta(DetailView):
    model = Empleado
    template_name = "Templates_Persona/detailview.html"

    # Seccion 8.9: Mas detalles del DetailView.
    # Funcion para enviar valores al template.
    def get_context_data(self, **kwargs):
        context = super(DetallaDeListaCompleta, self).get_context_data(**kwargs)
        context['Titulo'] = 'Prueba de context'
        return context

# ------------------------------------CreateVew------------------------------------------------

# 9.2 Redirección dentro de un CreateView – URL Name
# Clase - URL para utilizar en caso de ser exitoso el registro del empleado
class SuccessView(TemplateView):
    template_name = "Templates_Persona/Exitoso.html"


# Vista para registrar algo en un modelo
# 9.0 Vista CreateView
# Debemos de importarlo: Sección 8 vistas basadas en clases
# En fields debemos de indicarle con que campos vamos a trabajar, podemos incluir todos con all o solo especificar algunos
# tal como se muestra el ejempo.
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "Templates_Persona/createview.html"
    # fields = ['first_name', 'last_name', 'job', 'departamento']
    # fields = ('__all__')

    # 9.3 Form Valid en CreateView

    form_class = EmpleadoForm

    # 9.2 Redirección dentro de un CreateView – URL Name
    # uso del reverse_lazy para redireccion
    success_url = reverse_lazy('empleado_app:listar_empleados_administrador')

    # 9.3 Form Valid en CreateView
    # Funcion para hacer el full name
    def form_valid(self, form):
        # Necesitamos recuperartodo lo que se ingreso en el formulario
        # Creamos una instancia del formulario vinculada directamente a la base de datos.
        # Lo que quiere decir que en nuestra variable empleado tenemos todos los datos guardados
        empleado = form.save()
        # Ahora accedemos a los atributos de la instancia empleado.
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # Ahora para reflejar esto en la base de datos.
        empleado.save()
        # super para indicar que vamos a sobreescribir la función
        return super(EmpleadoCreateView, self).form_valid(form)


# ------------------------------UpdateView----------------------------
# 9.4 Update View
# Creamos una vista la cual nos permitira actualizar registros de nuestra base de datos
# Indicamos el modelo con el cual trabajaremos y los fields que actualizaremos, de igual manera el susses para cuando se es exitoso
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "Templates_Persona/update.html"
    fields = ['first_name',
              'last_name',
              'job',
              'departamento',
              'habilidades']
    success_url = reverse_lazy('empleado_app:listar_empleados_administrador')

    # Recuperar algo antes de eviarlo ald Form_valid
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        print(request.POST['last_name'])
        print()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)


# ---------------------------DeleteView-------------------------
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "Templates_Persona/deleteview.html"
    success_url = reverse_lazy('empleado_app:listar_empleados_administrador')

# 11.11 Listar empleados
class ListaEmpleadosAdmin(ListView):
    paginate_by = 5
    ordering = 'first_name'
    template_name = 'Templates_Persona/list_empleados.html'
    context_object_name = 'paginado'
    model = Empleado
