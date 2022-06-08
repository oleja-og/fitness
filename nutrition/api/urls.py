from django.urls import path
from . import views

urlpatterns = [
    path('', views.NutritionListCreateApiView.as_view()),
    path('male/', views.NutritiondmaleApiView.as_view()),
    path('woman/', views.NutritiondwomanApiView.as_view()),

]
