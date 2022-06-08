from django.views.generic import ListView, DetailView
from .models import Equipment


class EquipmentListView(ListView):
    queryset = Equipment.objects.all()
    context_object_name = 'equipment'
    paginate_by = 3
    template_name = 'equipment.html'


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipment_detail.html'
    context_object_name = 'equip'