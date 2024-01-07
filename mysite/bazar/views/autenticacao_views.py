from bazar.forms.login_forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, "bazar/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.data["email"], password=form.data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("eventos")

            messages.error(request, "Usuário ou senha inválidos.")

        context = {"form": form}
        return render(request, "bazar/login.html", context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")
