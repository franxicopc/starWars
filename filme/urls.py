from django.contrib import admin
from django.urls import path

from filme.views import add_filme, home, list_filmes

urlpatterns = [
    path('create/', add_filme, name='add_filme'),
    path('list/', list_filmes, name='list_filmes'),
    path('', home, name='home')
]