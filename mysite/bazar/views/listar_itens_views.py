from bazar.models import Evento, Item
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import View


class ListarItensView(View):
    def get(self, request, evento_id):
        agora = timezone.now()
        try:
            evento = Evento.objects.get(
                id=evento_id, data_inicio__lte=agora, data_fim__gte=agora
            )
        except Evento.DoesNotExist:
            return redirect("eventos")

        itens = Item.objects.filter(evento=evento)
        context = {"itens": itens, "evento": evento}

        return render(request, "bazar/itens-evento.html", context)
