from music.views import addMusic, music_list
from django.urls import path

from music.views import music_list, index
from django.contrib import admin

app_name = 'music'

urlpatterns = [
    path('music_list/', music_list, name='music_list'),
    path('add_music/', addMusic, name='addMusic'),
]