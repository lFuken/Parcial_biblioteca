from django.db import models

# Create your models here.
class autor(models.Model):
    Nombre = models.CharField(max_length=100)
    Nacionalidad = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.id)+ '-' + self.Nombre + '-' + self.Nacionalidad