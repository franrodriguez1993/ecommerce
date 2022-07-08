from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class NuevoProducto(forms.Form):
    modelo = forms.CharField(max_length=30,label="Modelo:")
    imagen = forms.CharField(max_length=400,label="Imagen:")
    marca = forms.CharField(max_length=30,label="Marca:")
    precio = forms.IntegerField(min_value=0,label="Precio:")
    

class NuevoEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre:")
    apellido = forms.CharField(max_length=30,label="Apellido:")
    email = forms.CharField(max_length=30,label="Email:")

    
    
class NuevoCliente(forms.Form):
    nombre = forms.CharField(max_length=30,label="Nombre:")
    apellido = forms.CharField(max_length=30,label="Apellido:")
    email = forms.CharField(max_length=30,label="Email:")




class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
        
class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        
        
class FormularioComentario(forms.Form):
    body= forms.CharField(max_length=255)