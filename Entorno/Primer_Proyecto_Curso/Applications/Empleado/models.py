from ckeditor.fields import RichTextField
from django.db import models

# 6.4 Modelos Relacionados – ForeingKey.
# 6.4.1: Para trabajar con llaves foreaneas, debemos importar la tabla con la cual trabajaremos.
from Applications.Departamento.models import Departamento

# Create your models here.
# 7.0 Administrador de Django
# 7.2 Personalizar Tablas en el Administrador de Django
# 7.2.1 Creamos el modelo Habilidades
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Mi Habilidad'
        verbose_name_plural = 'Habilidades de los empleados'

    def __str__(self):
        return self.habilidad

# ------------------------------------Modelo Empleado----------------------------------------------
# 6.4.2: Creamos el modelo
class Empleado(models.Model):
    # 6.4.3: Aquí creamos una tupla, para la parte del campo Job, el cual puede seleccionar alguno de todos esos trabajos.
    JOB_CHOISES = (
        ('0', 'Ayudante General'),
        ('1', 'Supervisor'),
        ('2', 'Encargado'),
        ('3', 'Contador'),
        ('4', 'Proveedor'),
        ('5', 'Director General'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)

    # 9.3 Form Valid en CreateView
    # Creación de nueva variable para concatenar datos (first_name y last_name)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)

    # 6.4.4: Aqui creamos el campo job, el cual selecciona de la tupla el job necesario.
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOISES)
    # 6.4.5: Aqui creamos la llave forane, apuntando a departamento.
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # Relación con el modelo Habilidades (muchos a muchos)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    # 7.0 Administrador de Django
    # 7.2 Personalizar Tablas en el Administrador de Django
    # Podemos cambiar el nombre representativo del modelo
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name + ' ' + self.full_name
        # return str(self.id) + '-' + self.first_name + ' ' + self.last_name
