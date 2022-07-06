from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos,name="productos"),
    path('empleados/',empleados,name="empleados"),
    path('clientes/',clientes,name="clientes"),
    path('about/',about,name="about"),
    path('crearproducto/',crear_producto,name="crear_producto"),
    path('crearempleado/',crear_empleado,name="crear_empleado"),
    path('crearcliente/',crear_cliente,name="crear_cliente"),
    path('buscarproducto/',buscar_producto,name='busqueda_producto'),
    path("base/",base),
]