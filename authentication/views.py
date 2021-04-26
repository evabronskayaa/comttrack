from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, LoginUserForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/authorization.html'
    success_url = reverse_lazy('home')


def success_login(request):
    name = request.user.username
    return HttpResponse(f"<h1>You're successfully logged in, {name}!</h1>")
