from django.urls import path
from .views import SignUpView, LoginUser, TaskCreateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('add_task/', TaskCreateView.as_view(), name='add_task')
]