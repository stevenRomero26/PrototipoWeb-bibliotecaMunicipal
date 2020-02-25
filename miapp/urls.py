
from django.urls import path, include

from .views import *

urlpatterns = [

   path('libros/', listar_libros),
    path('autores/', listar_Autores),
    path("",pagina),
    path("categorias/", lista_categorias),
    path("prestamos/", lista_prestamos),
    path("estudiantes/", lista_Estdiantes)
]
