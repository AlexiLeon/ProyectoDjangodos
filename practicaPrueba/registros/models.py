from django.db import models

class Alumnos(models.Model): #estructura de tabla
    matricula = models.CharField(max_length=12) #texto corto
    nombre = models.TextField() #texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True) #fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)


class Meta:
    verbose_name = 'Alumno'
    verbose_name_plural = 'Alumnos'
    ordering = ["-created"]

def __str__(self):
    return self.nombre

    
