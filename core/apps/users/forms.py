from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=("Почта"),
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Введите почту"}),
    )
    
    password = forms.CharField(
        label=("Введите пароль"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )

    error_messages = {
        "invalid_login": (
            "Пожалуйста, введите корректные почту и пароль. Учтите что "
            "оба поля могут быть чуствительны к регистру."
        ),
        "inactive": ("Этот аккаунт не активен"),
    }