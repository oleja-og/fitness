from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Services


class ServicesListView(ListView):
    queryset = Services.objects.all()
    paginate_by = 3
    template_name = 'services.html'
    context_object_name = 'services'


class ServicesDetailView(DetailView):
    model = Services
    template_name = "services_detail.html"
    context_object_name = 'service'
