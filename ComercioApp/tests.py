from django.test import TestCase
from .models import * 
# Create your tests here.


#Test para probar la creación de un empleado: 
class EmpleadosTest(TestCase):
    
    def setUp(self):
        Empleados.objects.create(nombre="Julian", apellido="Martinez",email="mjulian@gmail.com")
        
    def test_empleado_nombre(self):
        empleado = Empleados.objects.get(apellido="Martinez")
        self.assertEqual(empleado.nombre, "Julian")
    
    def test_empleado_creado(self):
        empleado = Empleados.objects.get(apellido="Martinez")
        self.assertNotEquals(empleado, None)
        
        
#Test para probar el límite de caracteres a la hora de crear un empleado: 
class EmpleadosErrorTest(TestCase):
    
    def setUp(self):
        Empleados.objects.create(nombre="Julianaijdkasjdaksjdaisjdasdjasjdasidjasidjqweqweqweqweqsdfdsfsdfsdfsdf", apellido="Martinez",email="mjuliansinarroba")
        
    def test_empleado_nombre(self):
        empleado = Empleados.objects.get(apellido="Martinez")
        self.assertEqual(empleado.nombre, "Julianaijdkasjdaksjdaisjdasdjasjdasidjasidjqweqweqweqweqsdfdsfsdfsdfsdf")
    
    def test_empleado_creado(self):
        empleado = Empleados.objects.get(apellido="Martinez")
        self.assertNotEquals(empleado, None)
        
        
        
        
#Prueba de creación de productos: 
class CreacionProductos(TestCase):
    
    def setUp(self):
        Productos.objects.create(modelo="G10", marca="Motorola",imagen="https://images.fravega.com/f500/5023dc40df851918551c3cd7387d9dd1.jpg",precio=75000)
        
    def test_producto_modelo(self):
        telefono = Productos.objects.get(marca="Motorola")
        self.assertEqual(telefono.modelo, "G10")
    
    def test_producto_creado(self):
        telefono = Productos.objects.get(marca="Motorola")
        self.assertNotEquals(telefono, None)
