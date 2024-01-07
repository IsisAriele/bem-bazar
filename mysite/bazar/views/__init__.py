from django.shortcuts import render

# Create your views here.


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/index.html", context)


def eventos(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/eventos.html", context)

def cadastroeventos(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/cadastro-eventos.html", context)