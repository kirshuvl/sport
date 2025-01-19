from django.contrib import admin
from django.urls import path
from core.apps.users.views import logout_user, main_page, UserLoginView, AdminDashboard, UserDashboard


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("", main_page, name="main-page"),
    path("dashboard/admin", AdminDashboard.as_view(), name='admin-dashboard'),
    path("dashboard/user", UserDashboard.as_view(), name='user-dashboard')

]
