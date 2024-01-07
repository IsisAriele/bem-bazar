from bazar.views.autenticacao_views import LoginView, LogoutView
from bazar.views.cadastro_usuarios_views import CadastroUsuarioView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", CadastroUsuarioView.as_view(), name="cadastro"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("eventos/", views.eventos, name="eventos"),
    path("cadastroeventos/", views.cadastroeventos, name="cadastroeventos"),
    path("cadastroitem/", views.cadastroitem, name="cadastroitem"),
]
