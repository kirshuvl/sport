from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from core.apps.users.forms import UserLoginForm


class UserLoginView(TemplateView):
    form_class = UserLoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if not request.user.is_anonymous:
            return redirect("main-page")
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if not request.user.is_anonymous:
            return redirect("main-page")
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("main-page")
        return render(request, self.template_name, context={"form": form})


def main_page(request):
    if request.user.is_anonymous:
        return redirect("login")
    elif request.user.status == "PT":
        return render(request, "users/user_main_page.html")
    return render(request, "users/admin_main_page.html")


def logout_user(request):
    logout(request)
    return redirect("login")