from django.shortcuts import render, HttpResponse

# Create your views here.

menu = """
<nav>
  <ul>
   
  </ul>
</nav>
"""

def Principal(request):
    return render(request, "inicio/principal.html")

def Contacto(request):
    return render(request, "inicio/contacto.html")


def Formulario(request):
    return render(request, "inicio/formulario.html")


def Ejemplo(request):
    return render(request, "inicio/ejemplo.html")