from rest_framework import generics
from ..models import Shedule, Visitation_record
from .serializers import SheduleSerializers, Vizitaion_recordSerializers


class SheduleApiView(generics.ListCreateAPIView):
    queryset = Shedule.objects.all()
    serializer_class = SheduleSerializers


class Vizitation_recordApiView(generics.ListCreateAPIView):
    queryset = Visitation_record.objects.all()
    serializer_class = Vizitaion_recordSerializers
