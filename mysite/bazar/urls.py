from bazar.views.autenticacao_views import LoginView, LogoutView
from bazar.views.cadastro_eventos_views import CadastroEventoView
from bazar.views.cadastro_itens_views import CadastroItemView
from bazar.views.cadastro_usuarios_views import CadastroUsuarioView
from bazar.views.listar_eventos_views import ListarEventosView
from bazar.views.listar_itens_views import ListarItensView
from bazar.views.reservar_item_views import ReservarItemView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", CadastroUsuarioView.as_view(), name="cadastro"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("eventos/", ListarEventosView.as_view(), name="eventos"),
    path("cadastroeventos/", CadastroEventoView.as_view(), name="cadastroeventos"),
    path(
        "evento/<int:evento_id>/cadastroitens",
        CadastroItemView.as_view(),
        name="cadastroitem",
    ),
    path("evento/<int:evento_id>/itens", ListarItensView.as_view(), name="itensevento"),
    path(
        "evento/<int:evento_id>/itens/<int:item_id>/reservar",
        ReservarItemView.as_view(),
        name="reservaritem",
    ),
]
