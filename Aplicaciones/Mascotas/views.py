from django.shortcuts import render,redirect
from .models import Mascota , Dueño ,Especie_Mascota
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.username == 'roderich':
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas o no autorizado.')
            return redirect('login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
   
    return render(request, 'home.html')

def gestionarMascota(request):
    mascotasListado = Mascota.objects.all()
    dueños = Dueño.objects.all()
    especies=Especie_Mascota.objects.all()
    
    
    return render(request, "gestionMascotas.html", {
        "mascotas": mascotasListado,
        "dueños": dueños,
        "especies":especies,
        
    })


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


def registrarEspecie(request):
    if request.method == "POST":
        nombre_especie = request.POST['txtNombre']
        Especie_Mascota.objects.create(nombre_especie=nombre_especie)
        return redirect('/gestionarEspecies') 

def eliminarEspecie(request ,id):
    especie = Especie_Mascota.objects.get(id=id)
    especie.delete()
    return redirect('/gestionarEspecie')

def edicionEspecie(request,rut):
    especie = Especie_Mascota.objects.get(id=id)
    return render(request,"edicionEspecie.html", {"especie":especie})

def editarEspecie(request):
    id=request.POST['txtId']
    nombre_especie=request.POST['txtNombre']

    especie = Especie_Mascota.objects.get(id=id)
    especie.id=id
    especie.nombre_especie=nombre_especie
    
    especie.save()
    return redirect('/gestionarEspecie')

def gestionarEspecie(request):
    especiesListado = Especie_Mascota.objects.all()
    return render(request, "gestionEspecies.html", {"especie": especiesListado})


