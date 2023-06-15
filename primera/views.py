from django.shortcuts import render
from tokenize import PseudoExtras
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import NameForm, InputForm, AuthorForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
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
        print(request.POST)
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

def datosform_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "datosform.html", context)

def authorform_view(request):
    context = {}
    #crear el objeto form
    form = AuthorForm(request.POST or None, request.FILES or None)
    #verificar si el formulario es valido
    if form.is_valid():
        #guardar datos del modelo
        form.save()
        return HttpResponseRedirect('/thanks/')
    
    context['form'] = form
    return render(request, "datosform.html", context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "registrado satisfactoriamente")
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
        return HttpResponseRedirect('/menu/') 
    
    form = UserRegisterForm()
    context = {"register_form": form}
    return render(request,"registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"iniciaste sesion como: {username}.")
                return HttpResponseRedirect('/menu')
            else:
                messages.error(request,"username o password Incorrectos")
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,"username o password Incorrectos")
            return HttpResponseRedirect('/login')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "Seha cerrado la sesion satisfactoriamente.")
    return HttpResponseRedirect('/menu')