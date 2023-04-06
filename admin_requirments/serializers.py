from rest_framework import serializers

from trippens.serializers import ActivitySerializer, AddonSerializer, PlaceSerializer, TrippensTourSerializer
from user_managment.serializers import CustomerSerializer
from .models import*

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

    
class BranchSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Branches
        fields = '__all__'


class BranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'



class UpdateBranchSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Branches
        fields = '__all__'



class VehicleListSerializer(serializers.ModelSerializer):
    place = TrippensTourSerializer()
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'



class UpdateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        exclude = ['place']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class UpdateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        exclude = ['place']


class RoomListSerializer(serializers.ModelSerializer):
    place = TrippensTourSerializer()

    class Meta:
        model = Rooms
        fields = '__all__'



class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'



class ListStaffSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer(read_only=True)
    branch = BranchCreateSerializer(read_only=True)
    class Meta:
        model = UserStaff
        fields = '__all__'



class CreateTourFormSerialiser(serializers.ModelSerializer):
    class Meta :
        model = TourForm
        fields = '__all__'

class ListTourFormSeraliser(serializers.ModelSerializer):
    customer = CustomerSerializer()
    rooms = RoomListSerializer()
    vehicles = VehicleListSerializer()
    class Meta :
        model = TourForm
        fields = '__all__'



class AddInetenarySerialiser(serializers.ModelSerializer):
    class Meta :
        model = CustomInetenary
        fields = '__all__'


class CustomItenearySerialiser(serializers.ModelSerializer):

    tour = TrippensTourSerializer()
    place = PlaceSerializer()
    addon = AddonSerializer(many=True)
    activivty = ActivitySerializer(many=True)



    class Meta :
        model = CustomInetenary
        fields = '__all__'

class AddToAcountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'

class ListAccountSerialiser(serializers.ModelSerializer):
    staff = ListStaffSerializer()
    customer = CustomerSerializer()

    class Meta:
        model = Accounts 
        fields = '__all__'



class UpdateAccountSerialiser(serializers.ModelSerializer):
        
    class Meta:
        model = Accounts 
        fields = ['gst','offer','total','is_veryfied']





class BookedToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTours
        fields = ['customer','staff','accounts','total']

class ListBookedTourSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    staff = ListStaffSerializer()
    accounts = ListAccountSerialiser()
    class Meta:
        model = BookedTours
        fields = '__all__'

class TransacionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacions
        fields = '__all__'


class UpdateTourSerializer(serializers.ModelSerializer):
    trans = TransacionsSerializer(read_only =True)
    customer = CustomerSerializer(read_only =True)
    staff = ListStaffSerializer(read_only =True)
    accounts = ListAccountSerialiser(read_only =True)
    class Meta:
        model = BookedTours
        fields = '__all__'



class AddAdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTours
        fields = ['payment_status','is_done']

