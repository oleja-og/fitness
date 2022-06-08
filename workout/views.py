from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WorkoutVideo


class WorkoutVideomaleListView(ListView):
    queryset = WorkoutVideo.objects.filter(gender='male')
    context_object_name = 'workouts'
    paginate_by = 3
    template_name = 'workout_male.html'


class WorkoutVideoListView(ListView):
    queryset = WorkoutVideo.objects.filter(gender='woman')
    context_object_name = 'workouts'
    paginate_by = 3
    template_name = 'workout_woman.html'


class WorkoutVideoDetailView(DetailView):
    model = WorkoutVideo
    template_name = 'workout_detail.html'
    context_object_name = 'work'


def index(request):
    return render(request, 'workout.html')


def index2(request):
    return render(request, 'workout_woman.html')
