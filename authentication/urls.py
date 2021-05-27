from django.urls import path
from django.views.generic import TemplateView

from .views import SignUpView, LoginUser, TaskCreateView, NotificationCreateForm, TaskView, complete_task

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(redirect_authenticated_user=True), name='login'),
    path('add_task/', TaskCreateView.as_view(), name='add_task'),
    path('notifications/', NotificationCreateForm.as_view(),
         name='notifications'),
    path('complete_task/', complete_task, name='complete'),
]