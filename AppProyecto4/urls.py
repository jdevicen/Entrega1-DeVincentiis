from django.urls import path
from AppProyecto4.views import *





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
    
]

