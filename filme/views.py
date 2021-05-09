from django.shortcuts import render, redirect
from .forms import FilmeForm
from .models import Filme

def home(request):
    return render(request, 'home.html')

def add_filme(request):
    form = FilmeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_filmes')
    return render(request, 'filme_form.html', {'form': form})


def list_filmes(request):
    lista_filmes = Filme.objects.all()
    return render(request, 'list_filmes.html', {'filmes': lista_filmes})