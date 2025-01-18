from django.contrib import admin
from django.urls import path
from core.apps.users.views import UserRegistration
from core.apps.users.views import UserProfile


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", UserRegistration.as_view(), name='register'),
    path('user_profile/', UserProfile.as_view(), name='user_profile'),
]
