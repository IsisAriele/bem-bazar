from bazar.forms.cadastro_eventos_forms import CadastroEventoForm
from bazar.models import Evento
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View


class CadastroEventoView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = CadastroEventoForm()
        context = {"form": form}
        return render(request, "bazar/cadastro-eventos.html", context)

    @method_decorator(login_required)
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
            return redirect("cadastroitem", evento_id=evento.id)

        context = {"form": form}
        return render(request, "bazar/cadastro-eventos.html", context)
