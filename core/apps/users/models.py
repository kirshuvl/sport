from django.db import models

from core.apps.common.models import TimedBaseModel
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUser(AbstractUser, TimedBaseModel):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        ("Никнейм"),
        max_length=150,
        unique=True,
        help_text=(
            "Не более 150 символов"
        ),
        validators=[username_validator],
        error_messages={
            "unique":("Пользователь с таким никнеймом уже существует"),
        },
    )

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=150,
    )

    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=150,
    )

    surname = models.CharField(
        verbose_name="Отчество",
        max_length=150,
        blank=True,
    )

    email = models.EmailField(
        verbose_name="Почта",
        blank=True,
    )

    bio = models.TextField(
        verbose_name="О себе",
        blank=True,
    )

    STATUS_CHOICES = [
        ("PT", "Участник"),
        ("TC", "Руководитель"),
    ]

    status = models.CharField(
        verbose_name="Статус пользователя",
        max_length=2,
        choices=STATUS_CHOICES,
        default="PT",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["pk"]
        db_table = "custom_users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
