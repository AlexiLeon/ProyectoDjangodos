from django.shortcuts import render
from .models import Alumnos

# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})