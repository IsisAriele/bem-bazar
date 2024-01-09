from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# O django já implementa autenticação por padrão atráves do User,
# por esse motivo ele será o suficiente para as demais implementações da minha aplicação.
class Evento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)

    @property
    def descricao_resumida(self):
        if len(self.descricao) > 74:
            return f"{self.descricao[:71]}..."

        return self.descricao

    @property
    def data_evento(self):
        meses_dict = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro",
        }

        mes_inicio = meses_dict[self.data_inicio.month]
        mes_fim = meses_dict[self.data_fim.month]

        data_inicio_formatada = f"{self.data_inicio.strftime('%d')} de {mes_inicio}"
        data_fim_formatada = f"{self.data_fim.strftime('%d')} de {mes_fim}"

        return f"{data_inicio_formatada} - {data_fim_formatada}"

    def save(self, *args, **kwargs):
        self.data_fim = datetime.strptime(self.data_fim, "%Y-%m-%d").replace(
            minute=59, hour=23, second=59
        )
        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} ----- {self.usuario.username}"


class Item(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="itens/")
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
