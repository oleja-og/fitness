from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterUser

urlpatterns = [
    # post views
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]