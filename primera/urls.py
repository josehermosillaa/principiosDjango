
from django.urls import path
from .views import IndexPageView, obtener_fecha, menu_view

urlpatterns = [
    # path('primera/', views.index, name=index)
    path('', IndexPageView.as_view(), name='index'),
    path('fecha/<str:name>/', obtener_fecha, name='fecha'),
    path('menu/', menu_view, name='menu'),
]
