from django.shortcuts import render

# Create your views here.


def Productos(request):
    
    return render(request,"comercioApp/productos.html",{})


def Empleados(request):
    
    return render(request,"comercioApp/empleados.html",{})




def base(request):
    return render(request,"comercioApp/base.html",{})