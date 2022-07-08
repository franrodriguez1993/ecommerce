from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

class Empleados(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True) #opcional
    
    class Meta:
        verbose_name_plural = "Empleados"


class Productos(models.Model):
    marca = models.CharField(max_length=30)
    imagen = models.CharField(max_length=400)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Productos"
    
class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True) #opcional
    
    class Meta:
        verbose_name_plural = "Clientes"
        

class Comentario(models.Model):
  autor = models.ForeignKey(User,on_delete=models.CASCADE)
  producto = models.ForeignKey(Productos, related_name="comments" ,on_delete=models.CASCADE)
  body = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)
    