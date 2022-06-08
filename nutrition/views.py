from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Nutrition


def index2(request):
    return render(request, 'nutrition_woman.html')

def index(request):
    return render(request, 'nutrition.html')


class NutritionmaleListView(ListView):
    queryset = Nutrition.objects.filter(gender='male')
    context_object_name = 'nutrition'
    paginate_by = 3
    template_name = 'nutrition_male.html'


class NutritionListView(ListView):
    queryset = Nutrition.objects.filter(gender='woman')
    context_object_name = 'nutrition'
    paginate_by = 3
    template_name = 'nutrition_woman.html'


class NutritionDetailView(DetailView):
    model = Nutrition
    template_name = 'nutrition_detail.html'
    context_object_name = 'nutrit'