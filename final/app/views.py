
from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *
import datetime
# Create your views here.


def home(request):
    return render(request, "app/home.html")

def crear(request):

    if request.method == 'POST':

        formulario = Formulario_Crear(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            empleado = Empleado(nombre=informacion["nombre"], usuario=informacion["usuario"], contraseña=informacion["contraseña"])
            empleado.save()
            formulario = Formulario_Crear()
            return render(request, "app/crear.html", {"nombre":informacion["nombre"], "form":formulario})
    else:
        formulario = Formulario_Crear()

    return render(request, "app/crear.html", {"form":formulario})


def ingresar(request):

    if request.method == "POST":

        formulario = Formulario_Registro(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            fecha = datetime.datetime.now().strftime('%d/%m/%Y')
            hora = datetime.datetime.now().strftime('%H:%M')
            registro = Registro_Ingreso(usuario=informacion["usuario"], horario=hora, fecha=fecha)
            registro.save()
            formulario = Formulario_Registro()
            return render(request, "app/ingreso.html", {"usuario": informacion["usuario"], "form":formulario})

    else:

        formulario = Formulario_Registro()

    return render(request, "app/ingreso.html", {"form": formulario})


def egresar(request):

    if request.method == "POST":

        formulario = Formulario_Registro(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data
            fecha = datetime.datetime.now().strftime('%d/%m/%Y')
            hora = datetime.datetime.now().strftime('%H:%M')
            registro = Registro_Egreso(usuario=informacion["usuario"], fecha=fecha, horario=hora)
            registro.save()
            formulario = Formulario_Registro()
            return render(request, "app/egreso.html", {"usuario": informacion["usuario"], "form":formulario})

    else:

        formulario = Formulario_Registro()

    return render(request, "app/egreso.html", {"form": formulario})


def buscar(request):

    if 'usuario' in request.GET:

        form = Formulario_Busqueda()
        usuario = request.GET['usuario']
        ingreso = Registro_Ingreso.objects.filter(usuario__icontains=usuario)
        egreso = Registro_Egreso.objects.filter(usuario__icontains=usuario)

        return render(request, "app/busqueda.html", {"form":form, "ingreso":ingreso, "egreso":egreso})

    else:
        form = Formulario_Busqueda()
        
    return render(request, "app/busqueda.html", {"form":form})
