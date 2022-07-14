from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('crear/', crear, name='crear'),
    path('ingresar/', ingresar, name="ingresar"),
    path('egresar/', egresar, name="egresar"),
    path('buscar/', buscar, name="buscar"),
]