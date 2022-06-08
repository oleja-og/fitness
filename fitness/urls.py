"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from main import views



urlpatterns = [
    path('', views.index, name='main'),
    path('about/', include('about.urls')),
    path('accounts/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('equipment/', include('equipment.urls')),
    path('news/', include('news.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('services/', include('services.urls')),
    path('shedule/', include('shedule.urls')),
    path('trainers/', include('trainers.urls')),
    path('workout/', include('workout.urls')),
    path('api/v1/news/', include('news.api.urls')),
    path('api/v1/accounts/', include('account.api.urls')),
    path('api/v1/sportroom/', include('main.api.urls')),
    path('api/v1/nutrition/', include('nutrition.api.urls')),
    path('api/v1/services/', include('services.api.urls')),
    path('api/v1/trainers/', include('trainers.api.urls')),
    path('api/v1/shedule/', include('shedule.api.urls')),
    path('api/v1/workout/', include('workout.api.urls')),

]
