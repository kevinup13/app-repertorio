from django.urls import path

from . import views

app_name = 'repertorio'

urlpatterns = [
    path('', views.lista_musicas, name='lista_musicas'),
    path('adicionar/', views.adicionar_musica, name='adicionar_musica'),
    path('editar/<int:pk>/', views.editar_musica, name='editar_musica'),
    path('excluir/<int:pk>/', views.excluir_musica, name='excluir_musica'),
]