from django.contrib import admin
from .models import Producto, Usuario, Rol
from .models import Cliente

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Rol)



