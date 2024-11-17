from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MusicaForm
from .models import Musica


@login_required
def lista_musicas(request):
    # Corrigido para ordenar por 'nome'
    musicas = Musica.objects.all().order_by('nome')
    return render(request, 'repertorio/lista_musicas.html', {'musicas': musicas})

@login_required
def adicionar_musica(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.adicionado_por = request.user
            musica.save()
            # Ajustado para incluir o namespace
            return redirect('repertorio:lista_musicas')
    else:
        form = MusicaForm()
    return render(request, 'repertorio/form_musica.html', {'form': form})

@login_required
def editar_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('repertorio:lista_musicas')
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'repertorio/form_musica.html', {'form': form})

@login_required
def excluir_musica(request, pk):
    musica = get_object_or_404(Musica, pk=pk)
    # Adicionado uma validação extra para admin e usuário
    if request.user.is_staff or request.user == musica.adicionado_por:
        musica.delete()
    return redirect('repertorio:lista_musicas')
