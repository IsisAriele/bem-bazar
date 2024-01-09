from bazar.forms.cadastro_eventos_forms import CadastroEventoForm
from bazar.models import Evento, Item, Reserva
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View


class ReservarItemView(View):
    @method_decorator(login_required)
    def get(self, request, evento_id, item_id):
        agora = timezone.now()
        try:
            evento = Evento.objects.get(
                id=evento_id, data_inicio__lte=agora, data_fim__gte=agora
            )
            item = Item.objects.get(id=item_id, evento=evento)
        except Evento.DoesNotExist:
            return redirect("eventos")

        if item.reservado:
            return redirect("itensevento", evento_id=evento_id)

        Reserva.objects.create(
            item=item,
            usuario=request.user,
        )

        return redirect("itensevento", evento_id=evento_id)
