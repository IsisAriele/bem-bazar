from django.shortcuts import render

# Create your views here.


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/index.html", context)


def cadastro(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/cadastro.html", context)


def login(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/login.html", context)


def eventos(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/eventos.html", context)
