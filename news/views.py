from django.shortcuts import render


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News


class NewsListView(ListView):
    queryset = News.objects.all()
    context_object_name = 'newsall'
    paginate_by = 3
    template_name = 'news.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'detail_news.html'
    context_object_name = 'news'


def news_detail(request, year, month, day, news):
    news = get_object_or_404(News, slug=news,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    return render(request, 'detail.html', {'news': news})