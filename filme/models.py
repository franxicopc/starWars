from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    duracao = models.CharField(max_length=10)
    capa = models.ImageField(upload_to='capa_filmes')
    bilheteria = models.CharField(max_length=50)
    ordem = models.IntegerField()
    trailer = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


class Musica(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    filme = models.ForeignKey(Filme, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
