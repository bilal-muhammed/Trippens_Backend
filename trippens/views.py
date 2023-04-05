from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from user_managment.models import CustomerResponse
from admin_requirments.models import CustomInetenary, TourForm
from admin_requirments.serializers import *
from .models import*
from .serializers import*

# Create your views here.

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = ListPlaceSerializer

class AddonList(generics.ListAPIView):
    queryset = Addon.objects.all()
    serializer_class = ListAddonSerializer 

class AddonUpdate(generics.RetrieveUpdateAPIView):
    queryset = Addon.objects.all()
    serializer_class = AddonSerializer


class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ListActvitySerializer

class UpdateActivity(generics.RetrieveUpdateAPIView):
    queryset = Activity.objects.all()
    serializer_class = UpdateActvitySerializer

class TourList(generics.ListCreateAPIView):
    queryset = TrippensTour.objects.all()
    serializer_class = TrippensTourSerializer

class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrippensTour.objects.all()
    serializer_class = TrippensTourSerializer



class AddPlace(APIView):
    def post(self, request):
        place_serializer = PlaceSerializer(data=request.data['place'])
        if place_serializer.is_valid():
            place_serializer.save()
            return Response({'place': place_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(place_serializer.errors, status=status.HTTP_400_BAD_REQUEST)









class AddTourDetails(APIView):

    def post(self, request):
        addon_serializer = CreateAddonSerializer(data=request.data['addon'])
        if addon_serializer.is_valid():
            addon_serializer.save()
            activity_serializer = ActivitySerializer(data=request.data['activity'])
            if activity_serializer.is_valid():
                activity_serializer.save()
                
                return Response({'addon': addon_serializer.data,
                                'activity': activity_serializer.data
                            }, status=status.HTTP_201_CREATED)
                        

            return Response(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print('error is here 1')
        return Response(addon_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                

class TourPlacesAPIView(generics.ListAPIView):
    serializer_class = GetPlaceSerializer

    def get_queryset(self):
        tour_id = self.kwargs['tour_id']
        return Place.objects.filter(tour_id=tour_id)
    


class PlacesAddonAPIView(generics.ListAPIView):
    serializer_class = GetAddonSerializer

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        return Addon.objects.filter(place=place_id)
    


class PlacesActivityAPIView(generics.ListAPIView):
    serializer_class = GetActivitySerializer

    def get_queryset(self):
        place_id = self.kwargs['place_id']
        return Activity.objects.filter(place=place_id)
    
class CreateTourForm(generics.CreateAPIView):
    queryset = TourForm.objects.all()
    serializer_class = CreateTourFormSerialiser


class AddInetenary(generics.CreateAPIView):
    queryset = CustomInetenary.objects.all()
    serializer_class = AddInetenarySerialiser

class CustomerResponseListByStaff(generics.ListAPIView):

    serializer_class = CustomerResponseSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return CustomerResponse.objects.filter(customer=id)
    

class CustomerForm(generics.ListAPIView):
    serializer_class = ListTourFormSeraliser
    def get_queryset(self):
        id = self.kwargs['id']
        return TourForm.objects.filter(customer = id)
        
