from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, LoginUserForm, CreateTaskForm


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


class TaskCreateView(CreateView):
    form_class = CreateTaskForm
    success_url = reverse_lazy('home')
    template_name = 'authentication/add_task.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_setter = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(TaskCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['task_setter'] = self.request.user
        return kwargs
