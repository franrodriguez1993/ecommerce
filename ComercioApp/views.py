from django.shortcuts import redirect, render

from ComercioApp.models import *

from .forms import *

# Create your views here.

def inicio(request):
    return render(request,"comercioApp/index.html",{})

def about(request):
    return render(request,"comercioApp/about.html",{})

def productos(request):
    
    productos = Productos.objects.all()  #Nos traemos todos los cursos de la DB
    return render(request,"comercioApp/productos.html",{"productos": productos})


def empleados(request):
    
    empleados = Empleados.objects.all()
    
    return render(request,"comercioApp/empleados.html",{"empleados":empleados})


def clientes(request):
    
    clientes = Clientes.objects.all()
    
    return render(request,"comercioApp/clientes.html",{"clientes":clientes})


def base(request):
    return render(request,"comercioApp/base.html",{})




def crear_producto(request):

    # post
    if request.method == "POST":

        formulario = NuevoProducto(request.POST)

        if formulario.is_valid():

            info_producto = formulario.cleaned_data
        
            producto = Productos(marca=info_producto["marca"],modelo=info_producto["modelo"],imagen=info_producto["imagen"] ,precio=int(info_producto["precio"]))

            producto.save() # guardamos en la bd
            
            return redirect("productos")

        else:

            return render(request,"comercioApp/crear_producto.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoProducto()

        return render(request,"comercioApp/crear_producto.html",{"form":formularioVacio})
    

def crear_empleado(request):

    # post
    if request.method == "POST":

        formulario = NuevoEmpleado(request.POST)

        if formulario.is_valid():

            info_empleado = formulario.cleaned_data
        
            empleado = Empleados(nombre=info_empleado["nombre"],apellido=info_empleado["apellido"] ,email=info_empleado["email"])

            empleado.save() # guardamos en la bd
            
            return redirect("empleados")

        else:

            return render(request,"comercioApp/crear_empleado.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoEmpleado()

        return render(request,"comercioApp/crear_empleado.html",{"form":formularioVacio})
    
    
def crear_cliente(request):

    # post
    if request.method == "POST":

        formulario = NuevoCliente(request.POST)

        if formulario.is_valid():

            info_cliente = formulario.cleaned_data
        
            cliente = Clientes(nombre=info_cliente["nombre"],apellido=info_cliente["apellido"] ,email=info_cliente["email"])

            cliente.save() # guardamos en la bd
            
            return redirect("clientes")

        else:

            return render(request,"comercioApp/crear_cliente.html",{"form":formulario})
    

    else: # get y otros

        formularioVacio = NuevoCliente()

        return render(request,"comercioApp/crear_cliente.html",{"form":formularioVacio})
    
    
def buscar_producto(request):
        if request.method == "POST":
            
            marca = request.POST["marca"]
            productos = Productos.objects.filter(marca__icontains=marca)
            
        else:
            productos = [] #Curso.objects.all()
        return render(request,"comercioApp/busqueda_producto.html",{"productos":productos})
      
      
def ver_producto(request, producto_id):
  producto = Productos.objects.get(id=producto_id)
  
  return render(request,"comercioApp/verProducto.html",{"producto":producto})