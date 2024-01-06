from bazar.views.cadastro_usuarios_views import CadastroUsuarioView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", CadastroUsuarioView.as_view(), name="cadastro"),
    path("login/", views.login, name="login"),
    path("eventos/", views.eventos, name="eventos"),
]
