from django.db import models

class Dueño(models.Model):
    rut=models.CharField(primary_key=True,max_length=10,unique=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=60)
    telefono=models.CharField(max_length=9)
    correo=models.CharField(max_length=50)
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre,self.rut)

class Especie_Mascota(models.Model):
    id=models.AutoField(primary_key=True,max_length=6)
    nombre_especie=models.CharField(max_length=50)
    def __str__(self):
        texto= "{0} (ID: {1})"
        return texto.format(self.nombre_especie,self.id)

class Mascota(models.Model):
    id=models.AutoField(primary_key=True ,unique=True)
    nombre_mascota=models.CharField(max_length=50)
    fecha_nac=models.DateField(max_length=10)
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)
    especie = models.ForeignKey(Especie_Mascota, on_delete=models.PROTECT)
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre_mascota,self.sexo)
    
    

