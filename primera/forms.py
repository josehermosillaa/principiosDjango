from django import forms
from .models import Author
#se importa la clase interna de Django forms, para la creacion de formularios

class NameForm(forms.Form):
    your_name = forms.CharField(label='Ingrese su Nombre:', max_length=100)


class InputForm(forms.Form):

    nombres = forms.CharField(max_length=200)
    apellidos = forms.CharField(max_length=200)
    prioridad = forms.IntegerField(widget=forms.TextInput,min_value=1, max_value=3)
    habilitado = forms.BooleanField()
    date = forms.DateField(widget=forms.SelectDateWidget)

    contrasena = forms.CharField(widget=forms.PasswordInput())

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        