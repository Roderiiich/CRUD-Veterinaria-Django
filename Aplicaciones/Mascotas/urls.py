from django .urls import path
from  Aplicaciones.Mascotas import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home', views.home, name='home'),
    path('gestionarMascota/', views.gestionarMascota, name='gestionarMascota'),
    path('registrarMascota/', views.registrarMascota, name='registrarMascota'),
    path('eliminarMascota/<id>', views.eliminarMascota, name='eliminarMascota'),
    path('edicionMascota/<id>', views.edicionMascota),
    path('editarMascota/', views.editarMascota),
    path('gestionarDueño/', views.gestionarDueño, name='gestionarDueño'),
    path('eliminarDueño/<rut>', views.eliminarDueño,name='eliminarDueño'),
    path('edicionDueño/<rut>', views.edicionDueño, name='edicionDueño'),
    path('editarDueño/', views.editarDueño),
    path('registrarDueño/', views.registrarDueño, name='registrarDueño'),

   
]