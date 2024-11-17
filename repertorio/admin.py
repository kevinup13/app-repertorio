from django.contrib import admin

from .models import Categoria, Musica


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'artista', 'categoria', 'adicionado_por', 'data_adicao')  # Alterado de 'titulo' para 'nome'
    list_filter = ('categoria', 'data_adicao')
    search_fields = ('nome', 'artista')  # Alterado de 'titulo' para 'nome'
