from django.db import models

# Create your models here.
class Usuario(models.Model):#creo tabla llamada Departamentos
    NumUsuario = models.IntegerField()
    NIF = models.CharField(max_length=20)
    Nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)+ '-' + str(self.NumUsuario) + '-' + self.NIF + '-' + self.Nombre + '-' + self.direccion  + '-' + self.telefono 