from django.urls import path
from . import views

urlpatterns = [
    # post views
    path('rules/', views.RulesListView.as_view(), name='rules'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts'),
]