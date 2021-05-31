"""comttrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from authentication.views import success_login, SignUpView, LoginUser, TaskCreateView, NotificationCreateForm, \
    user_logout, complete_task

urlpatterns = [
    path('', success_login, name='home'),
    path('admin/', admin.site.urls),
    #path('authentication/', include('authentication.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(redirect_authenticated_user=True), name='login'),
    path('add_task/', TaskCreateView.as_view(), name='add_task'),
    path('notifications/', NotificationCreateForm.as_view(),
         name='notifications'),
    path('logout/', user_logout, name='logout'),
    path('complete_task/', complete_task, name='complete'),
]
