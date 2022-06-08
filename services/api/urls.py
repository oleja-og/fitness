from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesListCreateApiview.as_view()),
    path('card/', views.CardListCreateApiview.as_view()),
    path('car_sale/', views.Card_saleListCreateApiview.as_view()),

]
