from django.db import models
from django.contrib.auth.models import User
 
class Evento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return f"{self.nome} ----- {self.usuario.username}"

class Item(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='itens/')
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ----- {self.evento.nome}"

class Reserva(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuario.username} ----- {self.item.nome}"
