from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=200) 
    lenguaje = models.CharField(max_length=200) 
    precio = models.CharField(max_length=10) 

    def __str__(self):
        return self.nombre