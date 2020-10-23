from django.db import models
from aplications.autor.models import autor

# Create your models here.

class Libro(models.Model):
    Codigo = models.IntegerField()
    Titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=30)
    Editorial = models.CharField(max_length=60)
    Numpage = models.IntegerField()
    codigo_autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+ '-' + str(self.Codigo) + '-' + self.Titulo + '-' + self.ISBN + '-' + self.Editorial  + '-' + str(self.Numpage)