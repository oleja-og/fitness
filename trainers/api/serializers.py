from rest_framework import serializers
from ..models import Trainers, Trainers_spec


class TrainersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trainers
        fields = '__all__'


class Trainers_specSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trainers_spec
        fields = '__all__'
