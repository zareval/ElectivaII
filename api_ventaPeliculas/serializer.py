from api_ventaPeliculas.models import pelicula
from rest_framework import serializers

class pelicula_serializer(serializers.ModelSerializer):
    class Meta:
        model=pelicula
        fields=['id', 'nombre', 'genero', 'duracion', 'director', 'pais', 'protagonistas', 'f_estreno', 'trailer', 'poster', 'protagonistas', 'price']