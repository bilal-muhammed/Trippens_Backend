from rest_framework import serializers
from admin_requirments.serializers import*
from trippens.serializers import TrippensTourSerializer
from .models import*
from admin_requirments.models import *
import datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['designation'] = user.designation.designation
        token['profile_pic'] = user.profile_pic.url if user.profile_pic else ''
        
        # ...

        return token


class CreateStaffSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserStaff
        fields = ['name','username','password','phone','address','branch','designation','adhar_no','profile_pic','image',]

    def create(self, validated_data):
        user = UserStaff.objects.create_user(**validated_data)
        return user

class UpdateStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStaff
        fields = '__all__'

class Branchserializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'

class UpdateStaffdetailsSerializer(serializers.ModelSerializer):
    # designation = DesignationSerializer()
    branch = serializers.PrimaryKeyRelatedField(queryset=Branches.objects.all())
    designation = serializers.PrimaryKeyRelatedField(queryset=Designation.objects.all())

    class Meta:
        model = UserStaff
        exclude = ['password','profile_pic','image'] 


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
   


class UpdateStaffSerializer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField()

    branch = Branchserializer()
    designation = DesignationSerializer(read_only = True)
    class Meta : 
        model = UserStaff
        fields = '__all__'
    def get_last_login(self, obj):
        if obj.last_login is None:
            return None
        return obj.last_login.strftime('%Y-%m-%d %H:%M:%S')

class ListCustomerSerializer(serializers.ModelSerializer):
    branch = Branchserializer(read_only=True)
    tours=TrippensTourSerializer(read_only=True)
    class Meta:
        model = Customers
        fields = '__all__'

class InstantEditSerializer(serializers.ModelSerializer):
    class Meta :
        model = Customers
        fields = ['phone','name']
    
class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'



class CreateCutomerSerializer(serializers.ModelSerializer):
    # branch = branchserializer()

    class Meta:
        model = Customers
        exclude = ['is_created','updated_to']





class CustomerSerializer(serializers.ModelSerializer):
    branch = Branchserializer()
    tours = TrippensTourSerializer()
    class Meta:
        model = Customers
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    branch = Branchserializer()
    designation = DesignationSerializer()
    class Meta:
        model = UserStaff
        fields = '__all__'

class AsignedCustomerSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    staff = StaffSerializer()
    class Meta:
        model = AssignedCustomer
        fields ='__all__'
    


class GetCustomerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class UserStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStaff
        fields = '__all__'

class GetAssignedCustomerSerializer(serializers.ModelSerializer):
    staff = UserStaffSerializer()
    customer = GetCustomerSerialiser()
    class Meta:
        model = AssignedCustomer
        fields = '__all__'



class LeaveRequestSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    class Meta:
        model = LeaveRequest
        fields = '__all__'


class StaffActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffActivity
        exclude = ['time_at']

class ListStaffActivitySerializer(serializers.ModelSerializer):
    staff = UserStaffSerializer()
    class Meta:
        model = StaffActivity
        fields = '__all__'

class ListResponseSerializer(serializers.ModelSerializer):

    staff = StaffSerializer()
    customer = GetCustomerSerialiser()

    class Meta: 
        model = CustomerResponse
        fields = '__all__'


class FixedIteneariesSerializer(serializers.ModelSerializer):
    class Meta :
        model = FixedItenearies
        fields = '__all__'