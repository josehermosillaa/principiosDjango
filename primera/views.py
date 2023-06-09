from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

# vista basada en clases


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
