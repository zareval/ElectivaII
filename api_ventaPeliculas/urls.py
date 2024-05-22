from django.urls import path
from .views import PeliculaView

urlpatterns= [
    path('creacionPelicula', PeliculaView.as_view(), name='creacionPelicula'),
    path('actualizacionPelicula/<int:pkid>/',PeliculaView.as_view(), name='actualizacion_pelicula'), #put
    path('eliminacionPelicula/<int:pkid>/',PeliculaView.as_view(), name='eliminacion_pelicula'), #delete
]