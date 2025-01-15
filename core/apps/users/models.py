from django.db import models
from django.contrib.auth.models import AbstractUser
from core.apps.common.models import TimedBaseModel


class CustomUser(AbstractUser, TimedBaseModel):
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

