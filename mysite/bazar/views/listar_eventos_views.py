from datetime import datetime

from bazar.forms.cadastro_itens_forms import CadastroItemForm
from bazar.models import Evento, Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View


class ListarEventosView(View):
    def get(self, request):
        agora = datetime.now()
        eventos = Evento.objects.filter(data_inicio__lte=agora, data_fim__gte=agora)
        context = {"eventos": eventos}
        return render(request, "bazar/eventos.html", context)
