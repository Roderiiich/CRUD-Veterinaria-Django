from django.shortcuts import render,redirect
from .models import Mascota , Dueño


def home(request):
    
    return render(request, "home.html")

def gestionarMascota(request):
    mascotasListado=Mascota.objects.all()
    return render(request, "gestionMascotas.html" , {"mascotas": mascotasListado})


def registrarMascota(request):
    nombre_mascota=request.POST['txtNombre']
    fecha_nac=request.POST['txtFechaNac']
    sexo=request.POST['txtSexo']

    mascotas=Mascota.objects.create(nombre_mascota=nombre_mascota,fecha_nac=fecha_nac,sexo=sexo)
    return redirect('/gestionarMascota')

def eliminarMascota(request,id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('/gestionarMascota')

def edicionMascota(request,id):
    mascota = Mascota.objects.get(id=id)
    return render(request,"edicionMascota.html",{"mascota":mascota})

def editarMascota(request):
    id=request.POST['txtId']
    nombre_mascota=request.POST['txtNombre']
    fecha_nac=request.POST['txtFechaNac']
    sexo=request.POST['txtSexo']

    mascota = Mascota.objects.get(id=id)
    mascota.id=id
    mascota.nombre_mascota=nombre_mascota
    mascota.fecha_nac=fecha_nac
    mascota.sexo=sexo
    mascota.save()
    return redirect('/')

def gestionarDueño (request):
    dueñosListado=Dueño.objects.all()
    return render(request, "gestionDueño.html" , {"dueño": dueñosListado})

def registrarDueño(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    direccion=request.POST['txtDireccion']
    telefono=request.POST['txtTelefono']
    correo=request.POST['txtCorreo']

    dueño=Dueño.objects.create(rut=rut,nombre=nombre,direccion=direccion,telefono=telefono,correo=correo)
    return redirect('/gestionarDueño')

def eliminarDueño(request ,rut):
    dueño = Dueño.objects.get(rut=rut)
    dueño.delete()
    return redirect('/gestionarDueño')

def edicionDueño(request,rut):
    dueño = Dueño.objects.get(rut=rut)
    return render(request,"edicionDueño.html", {"dueño":dueño})

def editarDueño(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']
    direccion=request.POST['txtDireccion']
    telefono=request.POST['txtTelefono']
    correo=request.POST['txtCorreo']

    dueño = Dueño.objects.get(rut=rut)
    dueño.rut=rut
    dueño.nombre=nombre
    dueño.direccion=direccion
    dueño.telefono=telefono
    dueño.correo=correo
    dueño.save()
    return redirect('/gestionarDueño')

def gestionarDueño(request):
    dueñosListado = Dueño.objects.all()
    return render(request, "gestionDueños.html", {"dueño": dueñosListado})
