from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, View, FormView

from .forms import CustomUserCreationForm, LoginUserForm, CreateTaskForm, CreateNotificationForm
from .models import Task, Notification


def get_tasks_for(username: str):
    return Task.objects.filter(executor__username=username)


def get_notifications():
    return Notification.objects.all()


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


class TaskView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.status == 'Employer':
            return TaskCreateView.as_view()(request, *args, **kwargs)
        else:
            return


class TaskCreateView(CreateView):
    form_class = CreateTaskForm
    success_url = reverse_lazy('add_task')
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

    def get_context_data(self, **kwargs):
        ctx = super(TaskCreateView, self).get_context_data(**kwargs)
        ctx['tasks'] = get_tasks_for(self.request.user.username)
        ctx['status'] = self.request.user.status
        return ctx


class TaskTrackView(FormView):
    pass


class NotificationCreateForm(CreateView):
    form_class = CreateNotificationForm
    success_url = reverse_lazy('notifications')
    template_name = 'authentication/notifications.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(NotificationCreateForm, self).get_form_kwargs(*args, **kwargs)
        kwargs['author'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        ctx = super(NotificationCreateForm, self).get_context_data(**kwargs)
        ctx['notifications'] = get_notifications()
        return ctx
