from rest_framework import serializers
from .models import*


class TeamAdvTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamAdventureTour
        fields = '__all__'
