from django.contrib import admin
from .models import Artista, Album, Cancion

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen_display', 'num_albumes', 'acciones')
    search_fields = ('nombre',)
    
    def imagen_display(self, obj):
        return obj.imagen.url if obj.imagen else 'No Image'
    imagen_display.short_description = 'Imagen'

    def num_albumes(self, obj):
        return obj.albumes.count()
    num_albumes.short_description = 'Número de Álbumes'

    def acciones(self, obj):
        return f'<a href="/admin/rap/artista/{obj.id}/change/">Editar</a>'
    acciones.short_description = 'Acciones'
    acciones.allow_tags = True

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anio', 'artista', 'num_canciones', 'acciones')
    list_filter = ('artista', 'anio')
    search_fields = ('nombre', 'artista__nombre')
    
    def num_canciones(self, obj):
        return obj.canciones.count()
    num_canciones.short_description = 'Número de Canciones'

    def acciones(self, obj):
        return f'<a href="/admin/rap/album/{obj.id}/change/">Editar</a>'
    acciones.short_description = 'Acciones'
    acciones.allow_tags = True

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'album', 'artista', 'acciones')
    list_filter = ('album',)
    search_fields = ('nombre', 'album__nombre', 'album__artista__nombre')
    
    def artista(self, obj):
        return obj.album.artista
    artista.short_description = 'Artista'

    def acciones(self, obj):
        return f'<a href="/admin/rap/cancion/{obj.id}/change/">Editar</a>'
    acciones.short_description = 'Acciones'
    acciones.allow_tags = True
