from django.shortcuts import render


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "bazar/index.html", context)
