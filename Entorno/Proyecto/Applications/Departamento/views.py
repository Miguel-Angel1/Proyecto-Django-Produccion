# 9.5 Formularios simples
# Importación de la vista generica FormView, vista que esta mas abajo de ocea en edit
# 11.8 Listar departamentos
# Importat vistas
from django.views.generic import ListView
from django.views.generic.edit import FormView

# Importación de modelo Empleado ubicado en otra ruta, ocea en applicatión
from Applications.Empleado.models import Empleado
# Importación del formulaio.
from .forms import NewDepartamentoForm
# Importación del modelo Departamento ubicado en esta mista app
from .models import Departamento

from django.urls import reverse_lazy


# 11.8 Listar departamento
# Creamos
class ListarDepartamento(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = 'Templates_Departamento/lista.html'


# Craeción de la clase de tipo FormView, la cual no esta asociada a ningun modelo y permitira trabajar con 2 modelos a la vez
class NewDepartamento(FormView):
    template_name = 'Templates_Departamento/nuevo_depa.html'
    # Llamada a form con el cual se construira el template
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('empleado_app:listar_empleados_administrador')

    # Creación del form_valid para validación antes de guardar en la base de datos.
    def form_valid(self, form):
        # Instacia del modelo departamento para poder interceptar los datos que se envian en el formulario
        depa = Departamento(
            # asiganción de los datos interceptados a los campos del modelo departamento
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shorname']
        )
        # Guardando los datos en la base de datos.
        depa.save()

        # Intercepción de datos para insertarlos en el modelo empleado
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        # Cración del object para recuperar datos e  insertarlos
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            departamento=depa,
        )

        return super(NewDepartamento, self).form_valid(form)
