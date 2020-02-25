from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def inicio(request):
    return HttpResponse("Hola mundo")

def pagina(request):
     return render(request,"miapp/idex.html")
    
def listar_libros(request):
    li = Libros.objects.all()
    return render(request,'miapp/index.html', {"listar_libros":li})
def listar_Autores(request):
    autores = Autores.objects.all()
    return render(request,'miapp/index1.html', {"listar_Autores":autores})
def lista_categorias(request):
    categoria=Categorias.objects.all()
    return render(request,"miapp/categoria.html",{"lista_categorias":categoria})  
def lista_prestamos(request):
    prestamoss=Prestamos.objects.all()
    return render(request,"miapp/prestamos.html",{"lista_prestamos":prestamoss})
def lista_Estdiantes(request):
    estudiantes=Estudiantes.objects.all()
    return render(request,"miapp/estudiantes.html",{"lista_Estdiantes":estudiantes})

