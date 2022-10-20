from django.urls import path
from AppProyecto4.views import *
from django.contrib.auth.views import LogoutView





urlpatterns = [
   
    path('', inicio, name="Inicio"),
    #path('Desarrollo/', desarrollo, name="Desarrollo"),
    path('produccion/', produccion, name="Produccionw"),
    path('Produccion/', Productions, name="Produccion"),
    path('Server/', Server, name="Server"),
    path('Sistemas/', sistemas, name="Sistemas"),
    path('Servers/', Servers, name="server"),
    path('buscarModelo/', busquedaModelo, name="busquedaModelo"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('login/', IniciarSesion, name='Login'),
    path('register/', registro, name='SignUP'),
    path('logout/', LogoutView.as_view(template_name="AppProyecto4/logout.html"), name='Logout'),
    path('editar/', editarUsuario, name='Editarusuario'),
    path('agregar/', agregarAvatar, name='Avatar'),
    path('agregarImagen/', agregarImagenes, name="AgregarImagen"),
    path('listimage/', images , name="imagelist"),

    #CRUD de Produccion
    path('leerProduccion',leerProduccions, name="ProduccionLeer"),
    path('Eliminarprod/<prodNombre>/',eliminarProduccion, name="EliminarProd"),
    path('editarProduccion/<prodNombre>/',editarProduccion, name="editarProduccion"),
    
    
    #CRUD de servidores
    #path('ListaServer/',leerServer, name="ServidoresLeer"),
    #path('Eliminarserver/<serverNom>/',eliminarServer, name="ServerEliminar"),
    #path('editarservers/<serverNom>/',editarServer, name="ServerEditar"),
    

    #CRUD de Servers usando Clases
    path('server/list/',ListaServer.as_view(), name="ServerLeer"),
    path('server/<int:pk>',DetalleServer.as_view(), name="ServerDetalle"),
    path("server/crear/",CrearServer.as_view(), name="ServerCrear"),
    path('server/editar/<int:pk>',ActualizarServer.as_view(), name="editarServer"),
    path('server/borrar/<int:pk>',BorrarServer.as_view(), name="EliminarServer"),


    
]

