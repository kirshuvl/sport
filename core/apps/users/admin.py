from django.contrib import admin
from core.apps.users.models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "status",
        "created_at",
        "updated_at",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "surname",
                    "email",
                    "bio",
                    "status",
                ),
            },
        ),
        (
            "Пароль",
            {
                "classes": ("wide",),
                "fields": ("password",),
            },
        ),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('last_name', 'first_name', 'surname', 'status', 'email', 'password1', 'password2'),
    }),
)