from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Artistas
    path('', views.lista_artistas, name='lista_artistas'),
    path('agregar/', views.agregar_artista, name='agregar_artista'),
    path('<slug:slug>/', views.detalles_artista, name='detalles_artista'),
    path('<int:artista_id>/editar/', views.editar_artista, name='editar_artista'),
    path('<int:artista_id>/eliminar/', views.eliminar_artista, name='eliminar_artista'),

    # Rutas para Álbumes
    path('<slug:slug>/agregar_album/', views.agregar_album, name='agregar_album'),
    path('<slug:slug>/<slug:album_slug>/editar/', views.editar_album, name='editar_album'),
    path('<slug:slug>/<slug:album_slug>/eliminar/', views.eliminar_album, name='eliminar_album'),

    # Ruta para detalles de álbum
    path('<slug:slug>/<slug:album_slug>/', views.detalles_album, name='detalles_album'),

    # Ruta para canciones de albúm
    path('<slug:slug>/<slug:album_slug>/agregar_cancion/', views.agregar_cancion, name='agregar_cancion'),
    path('<slug:slug>/<slug:album_slug>/editar_cancion/<int:cancion_id>/', views.editar_cancion, name='editar_cancion'),
    path('<slug:slug>/<slug:album_slug>/eliminar_cancion/<int:cancion_id>/', views.eliminar_cancion, name='eliminar_cancion'),
]
