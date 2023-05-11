from django.urls import path

from users.views import login, registration, logout, profile
from django.contrib import admin

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', registration, name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]

admin.site.index_title = 'Spotify'
admin.site.site_header = 'Spotify Admin'
