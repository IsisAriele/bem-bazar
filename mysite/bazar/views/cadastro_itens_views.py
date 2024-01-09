from bazar.forms.cadastro_itens_forms import CadastroItemForm
from bazar.models import Evento, Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View


class CadastroItemView(View):
    @method_decorator(login_required)
    def get(self, request, evento_id):
        try:
            evento = Evento.objects.get(id=evento_id, usuario=request.user)
        except Evento.DoesNotExist:
            return redirect("eventos")

        form = CadastroItemForm()
        context = {"form": form, "evento_id": evento.id}
        return render(request, "bazar/cadastro-item.html", context)

    @method_decorator(login_required)
    def post(self, request, evento_id):
        try:
            evento = Evento.objects.get(id=evento_id, usuario=request.user)
        except Evento.DoesNotExist:
            return redirect("eventos")

        form = CadastroItemForm(request.POST, request.FILES)
        if form.is_valid():
            Item.objects.create(
                evento=evento,
                nome=form.data["nome"],
                preco=form.data["preco"],
                foto=form.files["foto"],
            )
            messages.success(request, "Item cadastrado com sucesso!")
            return redirect("cadastroitem", evento_id=evento.id)

        context = {"form": form, "evento_id": evento.id}
        return render(request, "bazar/cadastro-item.html", context)
