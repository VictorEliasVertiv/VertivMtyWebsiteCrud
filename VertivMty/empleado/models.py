from django.db import models
import uuid

# Create your models here.

class Empleado(models.Model):
    ID_empleado = models.CharField(max_length=255)
    Nombre = models.CharField(max_length=255)
    Tipo = models.CharField(max_length=255)
    Area = models.CharField(max_length=255)
    Spot = models.CharField(max_length=255, blank = True)
    Supervisor = models.CharField(max_length=255, blank = True)
    Correo = models.EmailField(blank=True,default='default_email@vertiv.com')
    CorreoSupervisor = models.EmailField(blank=True,default='default_email@vertiv.com')
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.Nombre