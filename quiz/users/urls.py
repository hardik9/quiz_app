from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import quiz_home

urlpatterns = [
    path('', quiz_home, name='quiz-home'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
]
