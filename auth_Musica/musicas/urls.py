from django.urls import path
from . import views

urlpatterns = [
    path('list_musicas/', views.list_musicas, name='list_musicas'),
    path('create_musica/', views.create_musica, name="create_musica"),
    path('update_musica/<int:id>', views.update_musica, name="update_musica"),
    path('delete_musica/<int:id>', views.delete_musica, name="delete_musica"),    
]