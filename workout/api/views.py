from rest_framework import generics
from .serializers import WorkoutVideoSerializers
from ..models import WorkoutVideo


class WorkoutVideoListCreateApiView(generics.ListCreateAPIView):
    queryset = WorkoutVideo.objects.all()
    serializer_class = WorkoutVideoSerializers


class WorkoutmaleApiView(generics.ListAPIView):
    queryset = WorkoutVideo.objects.filter(gender='male')
    serializer_class = WorkoutVideoSerializers


class WorkoutwomanApiView(generics.ListAPIView):
    queryset = WorkoutVideo.objects.filter(gender='woman')
    serializer_class = WorkoutVideoSerializers
