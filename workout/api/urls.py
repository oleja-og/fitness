from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutVideoListCreateApiView.as_view()),
    path('male/', views.WorkoutmaleApiView.as_view()),
    path('woman/', views.WorkoutwomanApiView.as_view()),

]
