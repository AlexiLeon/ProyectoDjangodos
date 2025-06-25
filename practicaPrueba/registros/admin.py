from django.contrib import admin
from .models import Alumnos



class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Alumnos, AdministrarModelo)
