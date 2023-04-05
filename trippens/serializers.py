from rest_framework import serializers
from admin_requirments.models import UserStaff

from user_managment.models import CustomerResponse

from .models import*


class TrippensTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrippensTour
        fields = '__all__'

class ListPlaceSerializer(serializers.ModelSerializer):
    tour = TrippensTourSerializer()
    class Meta:
        model = Place
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    # tour = serializers.ReadOnlyField(source='tour.id')
    class Meta:
        model = Place
        # exclude = ['tour']
        fields = '__all__'

class GetPlaceSerializer(serializers.ModelSerializer):
    tour = serializers.ReadOnlyField(source='tour.id')
    class Meta:
        model = Place
        # exclude = ['tour']
        fields = '__all__'


class AddonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Addon
        fields = '__all__'

class ListActvitySerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Addon
        fields = '__all__'

class UpdateActvitySerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    class Meta:
        model = Addon
        fields = '__all__'

class ListAddonSerializer(serializers.ModelSerializer):
    place = PlaceSerializer()
    class Meta:
        model = Addon
        fields = '__all__'
    
class AddonSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    class Meta:
        model = Addon
        fields = '__all__'

class CreateAddonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Addon
        fields = '__all__'


class GetAddonSerializer(serializers.ModelSerializer):
    place =serializers.ReadOnlyField(source='place.id')
    class Meta:
        model = Addon
        fields = '__all__'


class GetActivitySerializer(serializers.ModelSerializer):
    place =serializers.ReadOnlyField(source='place.id')
    class Meta:
        model = Activity
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'


# class TourSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Tour
#         exclude =['is_active']
    
    

# class CreatedTourSerializer(serializers.ModelSerializer):
    
#     activity = ActivitySerializer(read_only=True)
#     addon = AddonSerializer(read_only=True)
#     place = PlaceSerializer(read_only=True)
#     name= TrippensTourSerializer(read_only=True)

#     class Meta:
#         model = Tour
#         fields = '__all__'



class staffSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserStaff
        fields = '__all__'
class CustomerResponseSerializer(serializers.ModelSerializer):

    staff = staffSerializer(read_only = True)
    class Meta:
        model = CustomerResponse
        fields = '__all__'