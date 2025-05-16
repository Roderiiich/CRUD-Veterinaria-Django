from django.contrib import admin
from Aplicaciones.Mascotas.models import Mascota,Especie_Mascota,Dueño

# Register your models here.

admin.site.register(Mascota)
admin.site.register(Especie_Mascota)
admin.site.register(Dueño)