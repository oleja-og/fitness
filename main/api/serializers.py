from rest_framework import serializers
from ..models import Sportroom


class SportroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sportroom
        fields = ('name',)
