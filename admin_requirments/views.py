
from rest_framework import viewsets,generics,status

from user_managment.models import CustomerResponse, Customers
from .views import*
from .models import*
from .serializers import*

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer





class BranchListAPIView(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer    

class BranchCreateAPIView(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchCreateSerializer

class BranchRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Branches.objects.all()
    serializer_class = UpdateBranchSerializer



class VehicleListAPIView(generics.ListAPIView):
    queryset = Vehicle.objects.all().order_by('id')
    serializer_class = VehicleListSerializer

class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleRetriveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = UpdateVehicleSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset =Rooms.objects.all().order_by('id')
    serializer_class = RoomListSerializer

class RoomCreateAPIView(generics.ListCreateAPIView):
    queryset =Rooms.objects.all()
    serializer_class = RoomSerializer


class RoomRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset =Rooms.objects.all()
    serializer_class = UpdateRoomSerializer


class DesignationList(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class DesignationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer



class TourFormDetails(generics.RetrieveAPIView):
    queryset = TourForm.objects.all()
    serializer_class = ListTourFormSeraliser







class CustomInetenaryList(generics.ListAPIView):
    serializer_class = CustomItenearySerialiser
    def get_queryset(self):
        form_id = self.kwargs['id']
        return CustomInetenary.objects.filter(form_id=form_id)

#>>>>>>> ADMIN DASHBOARD VIEWSETS <<<<<<<<#

from rest_framework.decorators import api_view
from datetime import datetime
from rest_framework.response import Response
#######################################################################################################

@api_view(['GET'])
def Customer_counts(request):
    customer_count = Customers.objects.all().count()
    today_count = Customers.objects.filter(is_created=datetime.now().date()).count()
    not_assigned = Customers.objects.filter(is_asigned=False).count()
    return Response({'customer_count': customer_count,
                     'today_count': today_count,
                     'not_assigned': not_assigned})


@api_view(['GET'])
def Booking_count(request):
    total_count = BookedTours.objects.all().count()
    today_count = BookedTours.objects.filter(date=datetime.now().date()).count()
    confirmed_count = BookedTours.objects.filter(is_done=True).count()
    Payment_pending = BookedTours.objects.filter(is_done=False).count()
    return Response({'total_count': total_count,
                     'today_count': today_count,
                     'confirmed_count': confirmed_count,
                     'Payment_pending':Payment_pending})

@api_view(['GET'])
def Followups_count(request):
    total_count = CustomerResponse.objects.all().count()
    today_count = CustomerResponse.objects.filter(followup_to=datetime.now().date(),is_followed=False).count()
    confirmed_count = CustomerResponse.objects.filter(is_followed=False).count()
    return Response({'total_count': total_count,
                     'today_count': today_count,
                     'confirmed_count': confirmed_count,
                    })










class AddAcounts(generics.CreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AddToAcountSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user.id
        staff = UserStaff.objects.get(id=user)
        serializer.save(staff=staff)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListAccounts(generics.ListAPIView):
    queryset = Accounts.objects.filter(is_done=False)
    serializer_class = ListAccountSerialiser

class ListAccountsCompleted(generics.ListAPIView):
    queryset = Accounts.objects.filter(is_done=True)
    serializer_class = ListAccountSerialiser


class VerifyAccounts(generics.RetrieveAPIView):
    queryset = Accounts.objects.all()
    serializer_class = ListAccountSerialiser

class UpdateAccounts(generics.RetrieveUpdateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = UpdateAccountSerialiser
    def perform_update(self, serializer):
        serializer.validated_data['is_veryfied'] = self.request.user.username
        serializer.validated_data['is_done'] = True
        serializer.save()



@api_view(['POST'])
def Create_booked_tour(request):
    serializer = BookedToursSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)



class ListBookedTours(generics.ListAPIView):
    queryset = BookedTours.objects.filter(is_done=False)
    serializer_class = ListBookedTourSerializer


class ListConfirmedTours(generics.ListAPIView):
    queryset = BookedTours.objects.filter(is_done=True)
    serializer_class = ListBookedTourSerializer

class GetBookedTour(generics.RetrieveAPIView):
    queryset = BookedTours.objects.all()
    serializer_class = UpdateTourSerializer



class AddAdvance(generics.RetrieveUpdateAPIView):
    queryset = BookedTours.objects.all()
    serializer_class = AddAdvanceSerializer

class AddTransation(generics.CreateAPIView):
    queryset = Transacions.objects.all()
    serializer_class = TransacionsSerializer

class ListTransactions(generics.ListAPIView):
    serializer_class = TransacionsSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return Transacions.objects.filter(bookedtours = id)



