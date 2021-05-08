from django.contrib import admin
from django.urls import path

from filme.views import add_filme, home

urlpatterns = [
    path('create/', add_filme, name='add_filme'),
    path('', home, name='home')
]