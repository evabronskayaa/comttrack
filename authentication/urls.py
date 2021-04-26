from django.urls import path
from .views import SignUpView, LoginUser

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login')
]