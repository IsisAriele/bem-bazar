from django.contrib import admin
from .models import Usuario, Item, Evento, Reserva

admin.site.register(Usuario)
admin.site.register(Item)
admin.site.register(Evento)
admin.site.register(Reserva)
