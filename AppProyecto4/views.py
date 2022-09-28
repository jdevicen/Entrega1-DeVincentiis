from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from AppProyecto4.forms import ServerForm, ProduccionForm
from django.http import HttpResponse
from AppProyecto4.models import *


# Create your views here.

def server(request):

     server =  Server(nombre="Server01", tipo="virtual")
     server.save()
     documentoDeTexto = f"--->Server: {server.nombre}   Modelo: {server.modelo}"


     return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppProyecto4/inicio.html")



#def desarrollo(request):
#
#     return render(request, "AppProyecto4/desarrollo.html")

def produccion(request):
    
      return render(request, "AppProyecto4/produccion.html")

def sistemas(request):

      return render(request, "AppProyecto4/sistemas.html")


def Servers(request):

      if request.method == "POST":  # Despues de dar enviar

            formulario1= ServerForm(request.POST)

            if formulario1.is_valid():

                  info = formulario1.cleaned_data

                  server = Server (nombre=info["nombre"], modelo=info["modelo"])
            
                  server.save()

                  return render(request, "AppProyecto4/inicio.html")

      else:

           formulario1 = ServerForm()

      return render(request, "AppProyecto4/server.html", {"form1":formulario1})

      #server = Server(nombre=request.POST["server"], modelo=request.POST["modelo"])


def Productions(request):

      if request.method == "POST":  # Despues de dar enviar

            formulario1= ProduccionForm(request.POST)

            if formulario1.is_valid():

                  info = formulario1.cleaned_data

                  prod = Produccion (nombre=info["nombre"], aplicacion=info["aplicacion"], dueño=info["dueño"])
            
                  prod.save()

                  return render(request, "AppProyecto4/inicio.html")

      else:

           formulario1 = ProduccionForm()

      return render(request, "AppProyecto4/produccion.html", {"form1":formulario1})

      #server = Server(nombre=request.POST["server"], modelo=request.POST["modelo"])      


def busquedaModelo(request):

      return render(request, "AppProyecto4/inicio.html")

def resultados(request):
      
      if request.GET["modelo"]:

         modelo=request.GET["modelo"]
         server = Server.objects.filter(modelo__icontains=modelo)

         return render(request, "AppProyecto4/inicio.html", {"server":server, "modelo":modelo })
      
      else:

         respuesta = "No hay datos."

      return HttpResponse(respuesta)


