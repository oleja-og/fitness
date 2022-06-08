from rest_framework import generics
from .serializers import NutritionSerializers
from ..models import Nutrition


class NutritionListCreateApiView(generics.ListCreateAPIView):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializers


class NutritiondmaleApiView(generics.ListAPIView):
    queryset = Nutrition.objects.filter(gender='male')
    serializer_class = NutritionSerializers


class NutritiondwomanApiView(generics.ListAPIView):
    queryset = Nutrition.objects.filter(gender='woman')
    serializer_class = NutritionSerializers
