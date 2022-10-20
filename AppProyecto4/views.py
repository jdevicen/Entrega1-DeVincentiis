from typing import List
from django.http.request import QueryDict
from django.shortcuts import render, redirect, HttpResponse
from AppProyecto4.forms import *
from django.http import HttpResponse
from AppProyecto4.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

#Vista para iniciar sesion
def IniciarSesion(request):

      if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():

                  usuario = form.cleaned_data.get("username")
                  contra = form.cleaned_data.get("password")

                  user = authenticate(username = usuario, password = contra)

                  if user:

                        login(request, user)

                        return render(request, "AppProyecto4/inicio.html", {"mensaje":f"Bienvenido {user}"})

            else:

                  return render(request, "AppProyecto4/inicio.html", {"mensaje":"Datos incorrectos."})

      else:

            form = AuthenticationForm()

      return render(request, "AppProyecto4/login.html", {"formulario":form})

#Vista para registrarse
def registro(request):

      if request.method == "POST":

            form = UsuarioRegistro(request.POST)

            if form.is_valid():

                  username = form.cleaned_data["username"]
                  form.save()
                  return render(request, "AppProyecto4/inicio.html", {"mensaje":"Usuario creado."})

      else:

            form = UsuarioRegistro()
      
      return render(request, "AppProyecto4/registro.html", {"formulario":form})

@login_required
def editarUsuario(request):

      usuario = request.user
      
      if request.method == "POST":

            form = FormularioEditar(request.POST)

            if form.is_valid():

                  info = form.cleaned_data

                  usuario.email = info["email"]
                  usuario.set_password(info["password1"])
                  usuario.first_name = info["first_name"]
                  usuario.last_name = info["last_name"]

                  usuario.save()

                  return render(request, "AppProyecto4/inicio.html")

      else:

            form= FormularioEditar(initial={"email":usuario.email,"first_name":usuario.first_name,"last_name":usuario.last_name,})

      return render(request, "AppProyecto4/editarPerfil.html", {"formulario":form, "usuario":usuario})



def server(request):

     server1 =  Server(nombre="Server01", tipo="virtual")
     server1.save()
     documentoDeTexto = f"--->Server: {server.nombre}   Modelo: {server.modelo}"


     return HttpResponse(documentoDeTexto)


#Pagina principal

def inicio(request):

      return render(request, "AppProyecto4/inicio.html")


# Vista para subir imagenes
@login_required
def agregarImagenes(request):

       if request.method == "POST":

           miFormulario = imagenFormulario(request.POST, request.FILES)

           if miFormulario.is_valid():

                informacion=miFormulario.cleaned_data

                addImage = ImagenServer(server=informacion["server"], imagen=informacion["imagen"])

                addImage.save()

                return render(request, "AppProyecto4/inicio.html")

       else:

            miFormulario=imagenFormulario()

       return render(request, "AppProyecto4/agregarimagen.html", {"form":miFormulario})

def images(request):

      imagenes = ImagenServer.objects.all()

 
      return render(request, "AppProyecto4/listimage.html", {"resultados":imagenes})


#def desarrollo(request):
#
#     return render(request, "AppProyecto4/desarrollo.html")

def produccion(request):
    
      return render(request, "AppProyecto4/produccion.html")

def sistemas(request):

      return render(request, "AppProyecto4/sistemas.html")


def Servers(request):

      if request.method == "POST":  # Despues de dar enviar

            formulario1= ServerForm(request.POST, request.FILES)

            if formulario1.is_valid():

                  info = formulario1.cleaned_data

                  server = Server (nombre=info["nombre"], modelo=info["modelo"], imagen=info["imagen"])
            
                  server.save()

                  return render(request, "AppProyecto4/inicio.html")

      else:

           formulario1 = ServerForm()

      return render(request, "AppProyecto4/server.html", {"form1":formulario1})

      #server = Server(nombre=request.POST["server"], modelo=request.POST["modelo"])

@login_required
def leerServer(request):

      servidores = Server.objects.all()

      contexto ={"equipo": servidores}

      return render(request, "AppProyecto4/server_list.html", contexto)

@login_required
def eliminarServer(request, serverNom):

       servers = Server.objects.get(nombre=serverNom)
       servers.delete()

       servidores = Server.objects.all()

       contexto={"equipos":servidores}

       return render(request, "AppProyecto4/server_list.html", contexto)


def editarServer(request, serverNom):

       servers = Server.objects.get(nombre=serverNom)
       
       if request.method == "POST":

           formulario1= ServerForm(request.POST)

           if formulario1.is_valid():

               info = formulario1.cleaned_data
               
               server.nombre = info["nombre"]
               server.modelo = info["modelo"]
               server.imagen = info["imagen"]

               servers.save()

               return render(request, "AppProyecto4/inicio.html")

       else:

            formulario1 = ServerForm(initial={"nombre":server.nombre, "modelo":server.modelo, "imagen":server.imagen})

       return render(request, "AppProyecto4/inicio.html", {"formulario1":formulario1, "nombre":serverNom})



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

@login_required
def leerProduccions(request):

      producciones = Produccion.objects.all()

      contexto ={"productions": producciones}

      return render(request, "AppProyecto4/leerProd.html", contexto)


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


@login_required
def eliminarProduccion(request, prodNombre):

      produccion = Produccion.objects.get(nombre=prodNombre)
      produccion.delete()

      producciones = Produccion.objects.all()

      contexto ={"productions": producciones}

      return render(request, "AppProyecto4/leerProd.html", contexto)


@login_required
def editarProduccion(request, prodNombre):

      produccion = Produccion.objects.get(nombre=prodNombre)

      if request.method == "POST":

         formulario1= ProduccionForm(request.POST)

         if formulario1.is_valid():

            info = formulario1.cleaned_data

            produccion.nombre = info["nombre"]
            produccion.aplicacion = info["aplicacion"]            
            produccion.dueño = info["dueño"]
            
            produccion.save()

            return render(request, "AppProyecto4/inicio.html")

      else:

           formulario1 = ProduccionForm(initial={"nombre":produccion.nombre, "aplicacion":produccion.aplicacion,"dueño":produccion.dueño})

      return render(request, "AppProyecto4/editarProduccion.html", {"form1":formulario1, "nombre":prodNombre})


class ListaServer(LoginRequiredMixin, ListView):

      model = Server
      

class DetalleServer(LoginRequiredMixin, DetailView):

      model = Server
      

class CrearServer(LoginRequiredMixin, CreateView):

      model = Server
      sucess_url = "AppProyecto4/curso/list"
      fields = ["nombre", "modelo", "imagen"]

class ActualizarServer(LoginRequiredMixin, UpdateView):

      model = Server
      sucess_url = "AppProyecto4/curso/list"
      fields = ["nombre", "modelo", "imagen"]


class BorrarServer(LoginRequiredMixin, DeleteView):

      model = Server
      sucess_url = "AppProyecto4/curso/list"



@login_required
def agregarAvatar(request):

      if request.method=="POST":

            form = AvatarFormulario(request.POST, request.FILES)

            if form.is_valid():

                  usuarioActual = User.objects.get(username=request.user)

                  avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

                  avatar.save()

                  return render(request, "AppProyecto4/inicio.html")

      else:

            form = AvatarFormulario()

      return render(request,"AppProyecto4/agregarAvatar.html", {"formulario":form})





 







 





