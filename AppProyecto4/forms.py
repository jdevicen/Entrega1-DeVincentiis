from django import forms

class ServerForm(forms.Form):

    nombre = forms.CharField()
    modelo = forms.IntegerField()


class ProduccionForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    aplicacion= forms.CharField(max_length=30)
    dueño= forms.EmailField()
