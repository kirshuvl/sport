from django.contrib.auth.forms import UserCreationForm
from core.apps.users.models import CustomUser
from django.db import models


class ExtendedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['surname'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Отчество"}
        self.fields['password1'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Пароль"}
        self.fields['status'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Статус"}
        self.fields['password2'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Повторите пароль"}
        self.fields['first_name'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Имя"}
        self.fields['last_name'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Фамилия"}
        self.fields['email'].widget.attrs = {"class": "form-control form-control-lg", "placeholder": "Почты"}

    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'surname', 'email', 'status',  'password1', 'password2']

