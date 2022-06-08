from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ServicesListView.as_view(), name='services'),
    path('<int:pk>', views.ServicesDetailView.as_view(), name='services_detail')
]