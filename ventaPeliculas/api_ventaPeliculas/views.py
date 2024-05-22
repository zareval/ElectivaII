from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_ventaPeliculas.models import pelicula
from api_ventaPeliculas.serializer import pelicula_serializer
import requests

# Create your views here.
class PeliculaView(APIView):
    
    def post(self, request, *args, **kwargs):
        data={
            'nombre':request.data.get('nombre'),
            'genero':request.data.get('genero'),
            'duracion':request.data.get('duracion'),
            'pais':request.data.get('pais'),
            'f_estreno':request.data.get('f_estreno'),
            'trailer':request.data.get('trailer'),
            'poster':request.data.get('poster'),
            'director':request.data.get('director'),
            'protagonistas':request.data.get('protagonistas'),
            'price':request.data.get('price')
        } 
        serializer = pelicula_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def get(self,request,*args,**kwargs):
        lista_peliculas=pelicula.objects.all()
        serializer_pelicula=pelicula_serializer(lista_peliculas,many=True)
        return Response(serializer_pelicula.data,status=status.HTTP_200_OK)
    
    def put(self,request,pkid):
        pelicula_consultada=pelicula.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            genero=request.data.get('genero'),
            duracion=request.data.get('duracion'),
            pais=request.data.get('pais'),
            f_estreno=request.data.get('f_estreno'),
            trailer=request.data.get('trailer'),
            poster=request.data.get('poster'),
            director=request.data.get('director'),
            protagonistas=request.data.get('protagonistas'),
            price=request.data.get('price')
        )
        return Response(pelicula_consultada,status=status.HTTP_200_OK)
    
    def delete(self,request,pkid):
        vehiculo_consultado=pelicula.objects.filter(id=pkid).delete()
        return Response(vehiculo_consultado,status=status.HTTP_200_OK)
    
    