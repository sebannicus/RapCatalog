from django import forms
from .models import Artista, Album, Cancion

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'imagen']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nombre', 'anio', 'imagen', 'artista']  # Incluye un campo para el artista

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre', 'album']  # Incluye un campo para el álbum
