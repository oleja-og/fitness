from rest_framework import generics
from ..models import Trainers, Trainers_spec
from .serializers import TrainersSerializers, Trainers_specSerializers


class TrainersApiView(generics.ListCreateAPIView):
    queryset = Trainers.objects.all()
    serializer_class = TrainersSerializers


class Trainers_specApiView(generics.ListCreateAPIView):
    queryset = Trainers_spec.objects.all()
    serializer_class = Trainers_specSerializers
