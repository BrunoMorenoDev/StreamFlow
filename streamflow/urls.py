from django.urls import path
from .views import (
    index,
    login_view,
    logout_view,
    home_view,
    usuarios_listar,
    usuarios_crear,
    usuarios_editar,
    usuarios_eliminar,
    artistas_listar,
    artistas_crear,
    artistas_editar,
    artistas_eliminar
)
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),

    path('usuarios/', usuarios_listar, name='usuarios_listar'),
    path('usuarios/crear/', usuarios_crear, name='usuarios_crear'),
    path('usuarios/editar/<int:idUsuario>/', usuarios_editar, name='usuarios_editar'),
    path('usuarios/eliminar/<int:idUsuario>/', usuarios_eliminar, name='usuarios_eliminar'),
    path('artistas/', artistas_listar, name='artistas_listar'),
    path('artistas/crear/', artistas_crear, name='artistas_crear'),
    path('artistas/editar/<int:idArtista>/', artistas_editar, name='artistas_editar'),
    path('artistas/eliminar/<int:idArtista>/', artistas_eliminar, name='artistas_eliminar'),
]