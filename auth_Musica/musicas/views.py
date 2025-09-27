from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import Musicas
from django.contrib.auth.decorators import login_required

# C -> POST
# R - GET
# U - PUT/PATCH
# D - DELETE

# Create your views here.



@login_required(login_url='/auth/login/')
def list_musicas(request):
    if request.method == 'GET':
        musicas = Musicas.objects.all()
        return render(request, 'list_musicas.html', {'musicas': musicas})

@login_required(login_url='/auth/login/')
def create_musica(request):
    if request.method == 'GET':
        return render (request, 'create_musica.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        album = request.POST.get('album')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        releaseDate = request.POST.get('releaseDate')
        
        musica = Musicas(name=name, album=album, artist=artist, genre=genre, releaseDate=releaseDate)
        musica.save()

        messages.add_message(request, constants.SUCCESS, 'Song successfully inserted!')
        return redirect('musicas:list_musicas')
 

@login_required(login_url='/auth/login/')
def update_musica(request, id):
    if request.method == 'GET':
        musicas = get_object_or_404(Musicas, id=id)
        return render(request, 'update_musica.html', {'musicas': musicas})
    
    if request.POST.get('_method') == 'PUT':
        musica = get_object_or_404(Musicas, id=id)
        name = request.POST.get('name')
        album = request.POST.get('album')
        artist = request.POST.get('artist')
        genre = request.POST.get('genre')
        releaseDate = request.POST.get('releaseDate')

        musica.name = name
        musica.album = album
        musica.artist = artist
        musica.genre = genre
        musica.release_date=releaseDate
        musica.save()
        messages.add_message(request, constants.SUCCESS, 'Updated successful')

        return redirect('musicas:list_musicas')


@login_required(login_url='/auth/login/')
def delete_musica(request, id):
    if request.POST.get('_method') == 'DELETE':
        musicas = get_object_or_404(Musicas, id=id)
        musicas.delete()
        messages.add_message(request, constants.SUCCESS, 'register vanished from the face of our planet!')
        return redirect('list_musicas')
   
    return redirect('musicas:list_musicas')


