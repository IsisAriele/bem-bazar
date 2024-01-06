from django.contrib import admin

from .models import Evento, Item, Reserva

admin.site.register(Item)
admin.site.register(Evento)
admin.site.register(Reserva)
