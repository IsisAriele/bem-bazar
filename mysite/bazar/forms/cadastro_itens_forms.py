from django import forms


class CadastroItemForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    preco = forms.DecimalField(label="Preço")
    foto = forms.ImageField(label="Upload de imagem do evento", required=False)
