
from django.urls import path
from .views import (
    IndexPageView, 
    obtener_fecha, 
    menu_view, 
    mostrar,
    prueba,
    get_name,
    gracias_view,
    datosform_view,
    authorform_view,
    register_view,
    login_view,
    logout_view,
    authors_view
    )

urlpatterns = [
    # path('primera/', views.index, name=index)
    path('', IndexPageView.as_view(), name='index'),
    path('fecha/<str:name>/<int:foto>/', obtener_fecha, name='fecha'),
    path('menu/', menu_view, name='menu'),
    path('mostrar/', mostrar, name='mostrar'),
    path('name/', get_name, name='get_name'),
    path('thanks/', gracias_view, name='gracias'),
    path('datosform/', datosform_view, name='datosform'),
    path('authorform/', authorform_view, name='authorform'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('authors/', authors_view, name='authors'),
    ##esta ruta es para probar cosas
    path('prueba/', prueba, name='prueba'),
]
