from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", max_length=255)
    password = forms.CharField(
        label="Senha", max_length=255, widget=forms.PasswordInput
    )
