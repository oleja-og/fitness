from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainersApiView.as_view()),
    path('trainers_spec/', views.Trainers_specApiView.as_view(), name='trainers_spec'),

]
