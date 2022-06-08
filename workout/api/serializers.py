from rest_framework import serializers
from ..models import WorkoutVideo


class WorkoutVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkoutVideo
        fields = "__all__"

