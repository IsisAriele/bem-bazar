from bazar.models import Evento
from django.shortcuts import render
from django.utils import timezone
from django.views import View


class ListarEventosView(View):
    def get(self, request):
        agora = timezone.now()
        eventos = Evento.objects.filter(data_inicio__lte=agora, data_fim__gte=agora)
        context = {"eventos": eventos}
        return render(request, "bazar/eventos.html", context)
