from rest_framework import serializers
from ..models import Nutrition


class NutritionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = "__all__"

