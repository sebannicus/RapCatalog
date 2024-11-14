from django.db import models
from django.utils.text import slugify

class Artista(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='artists/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='album/')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albumes')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.anio}) - {self.artista.nombre}"


class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones')

    def __str__(self):
        return self.nombre
