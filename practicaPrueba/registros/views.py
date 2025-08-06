from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages



# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()

#all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"registros/principal.html",{'alumnos':alumnos})


from django.shortcuts import render, redirect
from .forms import ComentarioContactoForm

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultarComentario')  
    else:
        form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})



def contacto(request):

    return render(request,"registros/contacto.html")



def consultarComentario(request):
        comentarios = ComentarioContacto.objects.all()
        return render(request,"registros/consultarComentario.html", {'comentarios': comentarios})



def eliminarComentarioContacto(request, id,
confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultarComentario.html",

{'comentarios':comentarios})

    return render(request, confirmacion, {'object':comentario})



#filter retorna registros que coincidan con los parametros como aqui el de TI
def consultar1(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/principal.html",{'alumnos':alumnos})



def consultar2(request):
    #con una sola condicion
    #multiples condiciones asicionado .filter() se analiza #como AND
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/principal.html",{'alumnos':alumnos})



def consultar3(request):
    #con una sola condicion
    #multiples condiciones asicionado .filter() se analiza #como AND
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request,"registros/principal.html",{'alumnos':alumnos})



def consultar4(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/principal.html",{'alumnos':alumnos})



def consultar5(request):
    #con una sola condicion
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/principal.html",{'alumnos':alumnos})



def consultar6(request):
    #con un rango de fechas
    fechaInicio = datetime.date(2025, 6, 20)
    #deberia ser 10 pq es el ultima fecha en el que se creo un usuario, pero se debe agregar un 10
    fechafin = datetime.date(2025, 7, 11)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechafin))
    return render(request,"registros/principal.html",{'alumnos':alumnos})


def consultar7(request):
    #                               tabla        campo      expresion
    alumnos=Alumnos.objects.filter(comentario__coment__contains='holaa')
    return render(request,"registros/principal.html",{'alumnos':alumnos})



#CONSULTA 1 yasta
def consultar8(request):
    fecha_inicio = datetime.date(2025, 7, 8)
    fecha_fin = datetime.date(2025, 7, 10)
    comentarios = ComentarioContacto.objects.filter(created__range=(fecha_inicio, fecha_fin))
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

#CONSULTA 2 yastaaa
def consultar9(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__exact="holaaaaaaaaaaaa")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

#CONSULTA 3
def consultar10(request): #                                          alexis777
    comentarios = ComentarioContacto.objects.filter(usuario__exact="nay")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})

#CONSULTA 4
def consultar11(request):
    lista_mensajes = ComentarioContacto.objects.values_list('mensaje')
    for mensaje in lista_mensajes:
        print(mensaje)
    return redirect('consultarComentario')

#CONSULTA 5
def consultar12(request):#                                      tiene que empezar con esa, no como hola etc
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="white")
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})



def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.files)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
                return render(request, "registros/archivos.html", {'archivo':Archivos})




def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request, "registros/principal.html", {'alumnos':alumnos})



def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",
    {'nombre':nombre})