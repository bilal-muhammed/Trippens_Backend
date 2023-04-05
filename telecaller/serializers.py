from rest_framework import serializers
from telecaller.models import UserLoginRecords

 
class UserLoginRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginRecords
        fields = '__all__'