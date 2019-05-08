from django.contrib import admin
from .models import Libro, Bodega, Cliente, Comuna

admin.site.register(Libro)
admin.site.register(Bodega)
admin.site.register(Cliente)
admin.site.register(Comuna)
# Register your models here.
