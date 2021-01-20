# 9.5 Formularios simples
# Importamos el modulo forms
from django import forms


# Creamos una clase formulario la cual no estara asociada a ningun modelo
# Creamos los campos que tendra
class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=50)
