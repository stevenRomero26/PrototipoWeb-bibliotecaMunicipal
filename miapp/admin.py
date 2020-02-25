from django.contrib import admin

from .models import Libros,Autores,Programa,Categorias,Prestamos,Estudiantes

admin.site.register(Libros)
admin.site.register(Autores)
admin.site.register(Categorias)
admin.site.register(Programa)
admin.site.register(Prestamos)
admin.site.register(Estudiantes)

