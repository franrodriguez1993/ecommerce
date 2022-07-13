from django.contrib import admin

from ComercioApp.models import *

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','email')
    search_fields = ('nombre', 'apellido''email')


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','precio','imagen')
    search_fields = ('nombre', 'marca','modelo','precio')
    
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','email')
    search_fields = ('nombre', 'apellido''email')
    
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('autor','producto','body','fecha')
    search_fields = ('autor','producto','body','fecha')



admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Productos,ProductosAdmin)
admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Comentario,ComentariosAdmin)
admin.site.register(Avatar)