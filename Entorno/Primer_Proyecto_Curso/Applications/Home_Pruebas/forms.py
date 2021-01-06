# 9.2 Model Form Parte 1
# Importamos el modulo form
from django import forms

# Importamos el modelo con el cual vamos a trabajar
from .models import Prueba


# Creamos un formulario basado en un modelo.
class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')

        # 9.4 Personalización de formularios
        # Plaeholder para campo de texto numero.
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aqui',
                }
            )
        }

    # 9.3 Validación en los Formularios
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un número mayor a 10')
        return cantidad
