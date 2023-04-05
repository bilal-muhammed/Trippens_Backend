from rest_framework import serializers
from .models import*


class GossipTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = GossipTour
        fields = '__all__'
