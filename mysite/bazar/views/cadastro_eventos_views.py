from bazar.forms.cadastro_eventos_forms import CadastroEventoForm
from bazar.models import Evento
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View


class CadastroEventoView(View):
    def get(self, request):
        form = CadastroEventoForm()
        context = {"form": form}
        return render(request, "bazar/cadastro-eventos.html", context)

    def post(self, request):
        form = CadastroEventoForm(request.POST)
        if form.is_valid():
            usuario = request.user
            evento = Evento.objects.create(
                usuario=usuario,
                nome=form.data["nome"],
                descricao=form.data["descricao"],
                data_inicio=form.data["data_inicio"],
                data_fim=form.data["data_fim"],
                poster=form.data["poster"],
            )
            return redirect("cadastroitem")

        context = {"form": form}
        return render(request, "bazar/cadastro-eventos.html", context)
