from django.urls import path

from AppProyecto4 import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('Desarrollo', views.cursos, name="desarrollo"),
    path('Producciom', views.profesores, name="produccion"),
    path('Server', views.estudiantes, name="server"),
    path('SO', views.entregables, name="so"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
   
]

