from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test

# Función de verificación para superusuario
def is_superuser(user):
    return user.is_superuser

# --- Vista para listar todos los artistas ---
def lista_artistas(request):
    query = request.GET.get('q')
    if query:
        artistas = Artista.objects.filter(Q(nombre__icontains=query))
    else:
        artistas = Artista.objects.all()
    return render(request, 'rap/lista_artistas.html', {'artistas': artistas})

# --- Vista para mostrar detalles de un artista ---
def detalles_artista(request, slug):
    artista = get_object_or_404(Artista, slug=slug)
    query = request.GET.get('q')
    if query:
        albumes = artista.albumes.filter(Q(nombre__icontains=query))
    else:
        albumes = artista.albumes.all()
    return render(request, 'rap/detalles_artista.html', {'artista': artista, 'albumes': albumes})

# --- Vista para mostrar detalles de un álbum ---
def detalles_album(request, slug, album_slug):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    query = request.GET.get('q')
    if query:
        canciones = album.canciones.filter(Q(nombre__icontains=query))
    else:
        canciones = album.canciones.all()
    return render(request, 'rap/detalles_album.html', {'artista': artista, 'album': album, 'canciones': canciones})

# --- Vistas para Artista ---
@login_required
@user_passes_test(is_superuser)
def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm()
    return render(request, 'rap/agregar_artista.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def editar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('detalles_artista', slug=artista.slug)
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'rap/editar_artista.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def eliminar_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    if request.method == 'POST':
        artista.delete()
        return redirect('lista_artistas')
    return render(request, 'rap/eliminar_artista.html', {'artista': artista})

# --- Vistas para Álbum ---
@login_required
@user_passes_test(is_superuser)
def agregar_album(request, slug):
    artista = get_object_or_404(Artista, slug=slug)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.artista = artista
            album.save()
            return redirect('detalles_artista', slug=artista.slug)
    else:
        form = AlbumForm()
    return render(request, 'rap/agregar_album.html', {'form': form, 'artista': artista})

@login_required
@user_passes_test(is_superuser)
def editar_album(request, slug, album_slug):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('detalles_artista', slug=artista.slug)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'rap/editar_album.html', {'form': form, 'artista': artista, 'album': album})

@login_required
@user_passes_test(is_superuser)
def eliminar_album(request, slug, album_slug):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    if request.method == 'POST':
        album.delete()
        return redirect('detalles_artista', slug=artista.slug)
    return render(request, 'rap/eliminar_album.html', {'artista': artista, 'album': album})

# --- Vistas para Canción ---
@login_required
@user_passes_test(is_superuser)
def agregar_cancion(request, slug, album_slug):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            cancion = form.save(commit=False)
            cancion.album = album
            cancion.save()
            return redirect('detalles_album', slug=artista.slug, album_slug=album.slug)
    else:
        form = CancionForm()
    return render(request, 'rap/agregar_cancion.html', {'form': form, 'artista': artista, 'album': album})

@login_required
@user_passes_test(is_superuser)
def editar_cancion(request, slug, album_slug, cancion_id):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    cancion = get_object_or_404(Cancion, id=cancion_id, album=album)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('detalles_album', slug=artista.slug, album_slug=album.slug)
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'rap/editar_cancion.html', {'form': form, 'artista': artista, 'album': album, 'cancion': cancion})

@login_required
@user_passes_test(is_superuser)
def eliminar_cancion(request, slug, album_slug, cancion_id):
    artista = get_object_or_404(Artista, slug=slug)
    album = get_object_or_404(Album, slug=album_slug, artista=artista)
    cancion = get_object_or_404(Cancion, id=cancion_id, album=album)
    if request.method == 'POST':
        cancion.delete()
        return redirect('detalles_album', slug=artista.slug, album_slug=album.slug)
    return render(request, 'rap/eliminar_cancion.html', {'artista': artista, 'album': album, 'cancion': cancion})
