from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.pagina_inicial, name='pagina_inicial'),

    # Rutas para Artistas
    path('artistas/', views.lista_artistas, name='lista_artistas'),
    path('artistas/agregar/', views.agregar_artista, name='agregar_artista'),
    path('artistas/<slug:slug>/', views.detalles_artista, name='detalles_artista'),
    path('artistas/<int:artista_id>/editar/', views.editar_artista, name='editar_artista'),
    path('artistas/<int:artista_id>/eliminar/', views.eliminar_artista, name='eliminar_artista'),

    # Rutas para Álbumes
    path('artistas/<slug:slug>/agregar_album/', views.agregar_album, name='agregar_album'),
    path('artistas/<slug:slug>/<slug:album_slug>/editar/', views.editar_album, name='editar_album'),
    path('artistas/<slug:slug>/<slug:album_slug>/eliminar/', views.eliminar_album, name='eliminar_album'),

    # Ruta para detalles de álbum
    path('artistas/<slug:slug>/<slug:album_slug>/', views.detalles_album, name='detalles_album'),

    # Rutas para Canciones
    path('artistas/<slug:slug>/<slug:album_slug>/agregar_cancion/', views.agregar_cancion, name='agregar_cancion'),
    path('artistas/<slug:slug>/<slug:album_slug>/editar_cancion/<int:cancion_id>/', views.editar_cancion, name='editar_cancion'),
    path('artistas/<slug:slug>/<slug:album_slug>/eliminar_cancion/<int:cancion_id>/', views.eliminar_cancion, name='eliminar_cancion'),
]