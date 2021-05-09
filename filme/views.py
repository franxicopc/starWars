from django.shortcuts import render, redirect, get_object_or_404
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


def get_filme(request, id):
    filme = get_object_or_404(Filme, pk=id)
    lista_musicas = filme.musica_set.all()

    print(lista_musicas)
    return render(request, 'filme_detalhes.html', {'filme': filme, 'musicas': lista_musicas})