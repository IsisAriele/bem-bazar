from django import forms


class CadastroUsuarioForm(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=255)
    last_name = forms.CharField(label="Sobrenome", max_length=255)
    email = forms.EmailField(label="E-mail", max_length=255)
    password = forms.CharField(
        label="Senha", max_length=255, widget=forms.PasswordInput
    )
