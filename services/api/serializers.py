from rest_framework import serializers
from ..models import Card, Services, Card_sale


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class Card_saleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card_sale
        fields = '__all__'
