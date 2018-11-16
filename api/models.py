from django.db import models

# Create your models here.
class Mascota(models.Model):
    idMascota=models.AutoField(primary_key=True)
    fotoMascota = models.ImageField(upload_to='FotosMascota/')
    nombreMascota = models.CharField(max_length = 20)
    raza = models.CharField(max_length = 20)
    descripcion = models.TextField()
    estado = models.CharField(max_length = 15)
