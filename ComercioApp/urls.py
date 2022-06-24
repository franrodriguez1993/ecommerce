from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('productos/', Productos,name="productos"),
    path('empleados/',Empleados,name="empleados"),
    path("base/",base)
]