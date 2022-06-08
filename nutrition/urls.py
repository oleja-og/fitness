from django.urls import path
from . import views

urlpatterns = [
    # post views

    path('', views.index, name='nutrition'),
    path('nutrition_male/', views.NutritionmaleListView.as_view(), name='nutrition_male'),
    path('nutrition_male/<int:pk>', views.NutritionDetailView.as_view(), name='nutrition_detail'),
    path('nutrition_women/', views.NutritionListView.as_view(), name='nutrition_woman'),
    path('nutrition_male/<int:pk>', views.NutritionDetailView.as_view(), name='nutrition_detail'),
]