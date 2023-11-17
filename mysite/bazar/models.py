from django.db import models
# from django.utils import timezone
# import datetime

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome
 
class Evento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data_inicio = models.DateTimeField('Data do início do evento')
    data_fim = models.DateTimeField('Data do fim do evento')
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.nome

class Item(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='itens/')
    descricao = models.CharField(max_length=200)
    preco = models.FloatField()

    def __str__(self):
        return self.descricao

class Reserva(models.Model):
    data = models.DateTimeField('Data da reserva')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    # item = models.ForeignKey(Item,  unique=True, on_delete=models.CASCADE)

