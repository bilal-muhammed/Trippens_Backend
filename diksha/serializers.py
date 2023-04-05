from rest_framework import serializers
from .models import*


class DikshaTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = DikshaTour
        fields = '__all__'
