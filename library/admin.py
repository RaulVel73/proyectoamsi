from django.contrib import admin
from .models import Categoria, Inventario, Clientes, Proveedores, Ventas, Productos

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Inventario)
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(Ventas)
admin.site.register(Productos)
