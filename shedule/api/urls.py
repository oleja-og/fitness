from django.urls import path
from . import views

urlpatterns = [
    path('', views.SheduleApiView.as_view()),
    path('vizitation_record/', views.Vizitation_recordApiView.as_view(), name='vizitation_record'),

]
