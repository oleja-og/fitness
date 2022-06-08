from django.urls import path
from . import views


urlpatterns = [
    path('', views.SportroomListViev.as_view(), name='sportroom'),

]
