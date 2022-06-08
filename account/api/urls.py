from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='user'),
    re_path(r'^(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='user_detail'),
]
