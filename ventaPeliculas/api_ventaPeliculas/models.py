from django.db import models


class pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracion = models.IntegerField()
    pais = models.CharField(max_length=50)
    f_estreno = models.DateField()
    trailer = models.URLField(max_length=200)
    poster = models.URLField(max_length=200) 
    director = models.CharField(max_length=50)
    protagonistas = models.CharField(max_length=100) 
    price = models.CharField(max_length=50, default=None, blank=True, null=True)
