from django import forms


class CadastroEventoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    descricao = forms.CharField(label="Descrição", max_length=255)
    data_inicio = forms.DateTimeField(
        label="Data do início do evento",
        widget=forms.DateInput(format="%d/%m/%Y", attrs={"type": "date"}),
    )
    data_fim = forms.DateTimeField(
        label="Data do fim do evento",
        widget=forms.DateInput(format="%d/%m/%Y", attrs={"type": "date"}),
    )
    poster = forms.ImageField(label="Upload de imagem do evento", required=False)
