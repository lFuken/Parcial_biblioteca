from django.db import models
from aplications.libro.models import Libro
from aplications.usuario.models import Usuario

# Create your models here.
class prestamo(models.Model):
    Fec_prestamo = models.DateField()
    Fec_devolucion = models.DateField()
    codigo_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    codigo_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+ '-' + str(self.Fec_prestamo) + '-' + str(self.Fec_devolucion) 