from rest_framework import serializers
from ..models import Shedule, Visitation_record


class SheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shedule
        fields = '__all__'


class Vizitaion_recordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitation_record
        fields = '__all__'
