from django.db import models
from django.contrib.auth.models import *


# Create your models here.

class Server(models.Model):

    def __str__(self):

         return f"Nombre: {self.nombre} -------- Modelo: {self.modelo}------- Imagen:{self.imagen}"

    nombre=models.CharField(max_length=40)
    modelo=models.IntegerField()
    imagen=models.ImageField(upload_to='servers', null=True)
  


#class Desarrollo(models.Model):
#    nombre= models.CharField(max_length=30)
#    aplicacion= models.CharField(max_length=30)
#    dueño= models.EmailField()

class Produccion(models.Model):

    
    def __str__(self):

         return f"Nombre: {self.nombre} -------- Aplicacion: {self.aplicacion}"

    nombre= models.CharField(max_length=30)
    aplicacion= models.CharField(max_length=30)
    dueño= models.EmailField()


class Sistemas(models.Model):
    nombre= models.CharField(max_length=30)
    aplicacion= models.CharField(max_length=30)


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

class ImagenServer(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="imagenes")
    imagen = models.ImageField(upload_to='servers', null=True, blank=True)







