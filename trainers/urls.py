from django.urls import path, re_path
from . import views

urlpatterns = [
    # post views
    path('', views.TrainersListView.as_view(), name='trainer'),
    path('<int:pk>', views.TrainersDetailView.as_view(), name='trainers_detail')

]