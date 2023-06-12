from django import forms

#se importa la clase interna de Django forms, para la creacion de formularios

class NameForm(forms.Form):
    your_name = forms.CharField(label='Ingrese su Nombre:', max_length=100)

