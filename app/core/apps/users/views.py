from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from core.apps.users.forms import ExtendedUserCreationForm
from django.contrib.auth import login, authenticate
# from django.contrib.auth.mixins import LoginRequiredMixin



class UserRegistration(CreateView):
    form_class = ExtendedUserCreationForm
    template_name = "users/register.html"

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user=user)
            return redirect('register')
        return render(request, self.template_name, context={"form": form})
    

class UserProfile(TemplateView):
    template_name = 'users/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user'] = user
        return context
    
    def get(self, request):
        if request.user.is_anonymous:
            return redirect('register')
        return render(request, self.template_name)




