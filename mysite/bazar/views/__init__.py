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

def cadastroitem(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/cadastro-item.html", context)

def itensevento(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/itens-evento.html", context)