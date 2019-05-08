from django.db import models


# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Libro(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    descrpcion = models.TextField(max_length=120)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    bodega = models.ForeignKey("Bodega", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.titulo)


class Bodega(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    comuna = models.ForeignKey("Comuna", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)


class Comuna(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.nombre)
