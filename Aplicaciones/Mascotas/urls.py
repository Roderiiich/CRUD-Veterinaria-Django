from django .urls import path
from  Aplicaciones.Mascotas import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),

    path('gestionarMascota/', views.gestionarMascota, name='gestionarMascota'),
    path('registrarMascota/', views.registrarMascota, name='registrarMascota'),
    path('eliminarMascota/<id>', views.eliminarMascota, name='eliminarMascota'),
    path('edicionMascota/<id>', views.edicionMascota,name='edicionMascota'),
    path('editarMascota/', views.editarMascota,name='editarMascota'),
    path('gestionarDueño/', views.gestionarDueño, name='gestionarDueño'),
    path('eliminarDueño/<rut>', views.eliminarDueño,name='eliminarDueño'),
    path('edicionDueño/<rut>', views.edicionDueño, name='edicionDueño'),
    path('editarDueño/', views.editarDueño),
    path('registrarDueño/', views.registrarDueño, name='registrarDueño'),

    path('registrarEspecie/', views.registrarEspecie, name='registrarEspecie'),
    path('gestionarEspecies/', views.gestionarEspecie, name='gestionarEspecies'),
    path('edicionEspecie/<id>/', views.edicionEspecie, name='edicionEspecie'),
    path('editarEspecie/<id>/', views.editarEspecie, name='editarEspecie'),
    path('eliminarEspecie/<id>/', views.eliminarEspecie, name='eliminarEspecie'),
    path('detalleDueño/<rut>/', views.detalleDueño, name='detalleDueño'),

    

   
]