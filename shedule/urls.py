from django.urls import path, re_path
from . import views

urlpatterns = [
    # post views

    path('', views.SheduleListView.as_view(), name='shedule')

]