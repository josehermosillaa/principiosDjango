from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import NameForm
import datetime

# vista basada en clases

class Persona:
    def __init__(self, nombre, apellido,login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login


class IndexPageView(TemplateView):
    template_name = 'index.html'

# vista basada en funciones


def index(request):
    return HttpResponse("HOLA ERICH")


def obtener_fecha(request, name, foto):
    fecha_actual = datetime.datetime.now()
    # print 'fecha: {fecha_actual}' NO!
    context = {
        'fecha': fecha_actual,
        'name': name,
        'frutas': ['Manzana', 'Mango', 'Naranja'],
        'foto': foto,
    }
    return render(request, 'fecha.html', context)


def menu_view(request):
    template_name = 'menu.html'
    return render(request, template_name)

def mostrar(request):
    persona = Persona("Juan", "Perez",True)
    items = ["Primero", "Segundo", "Tercero", "Cuarto"]
    context = {"nombre": persona.nombre, "apellido": persona.apellido,"login":persona.login, "items":items}
    
    return render(request, 'seguro.html', context)
    
def prueba(request):
    template_name = 'formulario.html'
    return render(request, template_name)


def get_name(request):
    #si se trata de una solicitud post, necesitamos procesar los datos del formulario!
    if request.method == 'POST':
        #crea una instancia de formulario y se completa con los datos de la solicitud :
        form = NameForm(request.POST)
        #comprobar si los datos son valdios
        if form.is_valid():
            # procesan los dastos en form.cleaned_data segun sea necesario
            #...
            #redirigimos a una nueva url
            return HttpResponseRedirect('/thanks/')
    #si es un get o cualquier oytro metodo crearemos un formulario en blanco
    else:
        form = NameForm()
        context = {'form': form}
    return render(request, 'name.html', context)

def gracias_view(request):
    return HttpResponse('<h1>Datos ingresados correctamente!</h1>')