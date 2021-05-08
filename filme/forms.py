from django.forms import ModelForm
from .models import Filme


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano', 'duracao', 'capa', 'bilheteria', 'ordem', 'trailer']

