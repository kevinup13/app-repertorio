from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField(max_length=200)  # Este é o título da música
    artista = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    letra = models.TextField(blank=True)
    acordes = models.TextField(blank=True)
    data_adicao = models.DateTimeField(auto_now_add=True)
    adicionado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.artista}"
