from rest_framework import generics
from ..models import Sportroom
from .serializers import SportroomSerializers


class SportroomListViev(generics.ListAPIView):
    queryset = Sportroom.objects.all()
    serializer_class = SportroomSerializers
