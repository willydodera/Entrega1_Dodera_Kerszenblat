from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre= models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

class Registro_Ingreso(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)


class Registro_Egreso(models.Model):
    usuario = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)


