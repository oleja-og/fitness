from rest_framework import generics
from ..models import Services, Card_sale, Card
from .serializers import ServicesSerializers, CardSerializers, Card_saleSerializers


class ServicesListCreateApiview(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


class CardListCreateApiview(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers


class Card_saleListCreateApiview(generics.ListCreateAPIView):
    queryset = Card_sale.objects.all()
    serializer_class = Card_saleSerializers
