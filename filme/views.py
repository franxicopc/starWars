from django.shortcuts import render, redirect
from .forms import FilmeForm

def home(request):
    return render(request, 'home.html')

def add_filme(request):
    form = FilmeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'filme_form.html', {'form': form})