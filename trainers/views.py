from django.views.generic import ListView, DetailView
from .models import Trainers


class TrainersListView(ListView):
    queryset = Trainers.objects.all()
    paginate_by = 3
    template_name = 'trainers.html'
    context_object_name = 'trainers'


class TrainersDetailView(DetailView):
    model = Trainers
    template_name = 'trainers_detail.html'
    context_object_name = 'trainer'



