from django.db import models
from django.forms import DateField
from datetime import date, datetime

# Create your models here.
class Familia(models.Model):
    
    nombre = models.CharField(max_length=25,default= '-')
    apellido = models.CharField(max_length=25, default= 'Dato privado')
    birth_date= models.DateField()
    edad = models.IntegerField(default= 0)
    ocupacion = models.CharField(max_length=25, default= 'No se especifica')
    p = models.CharField(max_length= 15, default= 'No se especifica parentezco')