from django.urls import path, re_path
from . import views

urlpatterns = [
    # post views

    path('', views.NewsListView.as_view(), name='news'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.news_detail),
    path('<int:pk>', views.NewsDetailView.as_view(), name='detail_news'),

]