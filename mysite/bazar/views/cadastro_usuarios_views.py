from bazar.forms.cadastro_usuarios_forms import CadastroUsuarioForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View


class CadastroUsuarioView(View):
    def get(self, request):
        form = CadastroUsuarioForm()
        context = {"form": form}
        return render(request, "bazar/cadastro.html", context)

    def post(self, request):
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(
                    first_name=form.data["first_name"],
                    last_name=form.data["last_name"],
                    username=form.data["email"],
                    email=form.data["email"],
                    password=form.data["password"],
                )
                messages.success(request, "Usuário cadastrado com sucesso!")
                return redirect("login")
            except Exception:
                messages.error(request, "Usuário já cadastrado")

        context = {"form": form}
        return render(request, "bazar/cadastro.html", context)
