from django.urls import path
from . import views

urlpatterns = [
    # post views

    path('', views.index, name='workout'),
    path('workout_male/', views.WorkoutVideomaleListView.as_view(), name='workout_male'),
    path('workout_detail/<int:pk>', views.WorkoutVideoDetailView.as_view(), name='detail_male'),
    path('workout_woman/', views.WorkoutVideoListView.as_view(), name='workout_woman'),
    path('workout_detail/<int:pk>', views.WorkoutVideoDetailView.as_view(), name='detail_woman'),

]