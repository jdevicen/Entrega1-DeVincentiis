from django.db import models

# Create your models here.

class Server(models.Model):

    nombre=models.CharField(max_length=40)
    modelo = models.IntegerField()


class Desarrollo(models.Model):
    nombre= models.CharField(max_length=30)
    aplicacion= models.CharField(max_length=30)
    dueño= models.EmailField()

class Produccion(models.Model):
    nombre= models.CharField(max_length=30)
    aplicacion= models.CharField(max_length=30)
    dueño= models.EmailField()


class SO(models.Model):
    nombre= models.CharField(max_length=30)
    aplicacion= models.CharField(max_length=30)