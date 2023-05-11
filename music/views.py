from music.models import Album, Music
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .form import AddMusicForm


def index(request):
    return render(request, 'music/index.html')


def music_list(request):
    music = list(Music.objects.all().values())
    return render(request, 'music/music_list.html', {
        'music': music
    })


def addMusic(request):
    form = AddMusicForm()

    if request.POST:
        form = AddMusicForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            album = form.cleaned_data.get('album')
            if album:
                music_album = Album.objects.get_or_create(name=album)
                print(music_album)
                instance.album = music_album[0]
                instance.save()
                return redirect("music:music_list")
            else:
                instance.save()
                return redirect("music:music_list")

        else:
            print("no", form.data)

    return render(request, 'music/addMusic.html', {
        'form': form
    })
