from django import forms


class Formulario_Crear(forms.Form):
    nombre = forms.CharField()
    usuario = forms.CharField()
    contraseña = forms.CharField()

class Formulario_Registro(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField()

class Formulario_Busqueda(forms.Form):
    usuario = forms.CharField()

