from django.db import models

class Libros(models.Model):
     
      nombre = models.CharField(max_length=100)
      autor = models.CharField(max_length=100)
      def __str__(self):
        return self.nombre
class Autores(models.Model):
     
      nombre = models.CharField(max_length=100)
     
     
      def __str__(self):
        return self.nombre
class Categorias(models.Model):
     
      nombre = models.CharField(max_length=100)
     
     
      def __str__(self):
        return self.nombre
class Prestamos(models.Model):
     
      nombre = models.CharField(max_length=100)
      Estudiante = models.CharField(max_length=100)
     
      def __str__(self):
        return self.nombre.Estudiante
class Programa(models.Model):
     
      nombre = models.CharField(max_length=100)
    
      semestre=models.CharField(max_length=100)
      def __str__(self):
        return self.nombre

     


class Estudiantes(models.Model):
     
      nombre = models.CharField(max_length=100)
      apellidos = models.CharField(max_length=100)
      direccion = models.CharField(max_length=200)
      telefono=models.CharField(max_length=100)

      def __str__(self):
        return self.nombre

