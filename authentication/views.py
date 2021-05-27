from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, View, FormView

from .forms import CustomUserCreationForm, LoginUserForm, CreateTaskForm, CreateNotificationForm
from .models import Task, Notification

from django.contrib.auth.mixins import LoginRequiredMixin


def get_tasks_for(username: str):
    return Task.objects.filter(executor__username=username, completed=False)


def get_completed_tasks():
    return Task.objects.filter(completed=True)


def get_all_tasks():
    return Task.objects.all()


def get_notifications():
    return Notification.objects.all().order_by('-created_at')


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


class TaskCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateTaskForm
    success_url = reverse_lazy('add_task')
    template_name = 'authentication/add_task.html'

    login_url = 'authentication/'
    redirect_field_name = 'login'

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
        ctx['all_tasks'] = get_all_tasks()
        ctx['completed_tasks'] = get_completed_tasks()
        ctx['notifications'] = get_notifications()
        return ctx


def complete_task(request):
    args = request.POST
    for key in args:
        try:
            key = int(key)
            task = Task.objects.get(id=key)
            task.completed = True
            task.save()
        except Exception:
            pass

    return HttpResponseRedirect(reverse('add_task'))


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
        ctx['status'] = self.request.user.status
        return ctx
