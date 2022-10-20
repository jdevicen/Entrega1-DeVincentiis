from django import forms
from AppProyecto4.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppProyecto4.models import Avatar, ImagenServer

class ServerForm(forms.Form):


    nombre = forms.CharField()
    modelo = forms.IntegerField()
    imagen = forms.ImageField()
    


class ProduccionForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    aplicacion= forms.CharField(max_length=30)
    dueño= forms.EmailField()


class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen", "usuario"]

class imagenFormulario(forms.ModelForm):

    class Meta:
        model = ImagenServer
        fields = ["imagen", "server"]



