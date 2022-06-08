from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('', views.EquipmentListView.as_view(), name='equipment'),
    path('<int:pk>', views.EquipmentDetailView.as_view(), name='equipment_detail'),
]