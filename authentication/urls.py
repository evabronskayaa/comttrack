from django.urls import path
from django.views.generic import TemplateView

from .views import SignUpView, LoginUser, TaskCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('add_task/', TaskCreateView.as_view(), name='add_task'),
    path('notifications/', TemplateView.as_view(template_name="authentication/notifications.html"),
         name='notifications'),
]