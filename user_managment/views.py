from .models import*
from .serializers import*
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_requirments.models import UserStaff
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
# Create your views here.
from rest_framework import permissions

# /////////////////////////////////
   

class setPagination(PageNumberPagination):
    page_size = 10 

# //////////////////////////////////////


class Updatestaff(generics.RetrieveUpdateAPIView):
    queryset = UserStaff.objects.all()
    serializer_class = UpdateStaffSerializer


@api_view(['GET'])
def check_username(request, username):
    user = UserStaff.objects.filter(username=username)
    username_exists = True if user else False
    return Response({'exists': username_exists})




class UserRegistrationView(APIView):
    serializer_class = CreateStaffSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            success_message = "New Staff Registered successfully."
            response_data = serializer.data
            response_data["success_message"] = success_message
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListStaff(generics.ListAPIView):
    queryset = UserStaff.objects.filter(designation = 12)
    serializer_class = StaffSerializer

class paginatedStaff(generics.ListAPIView):
    queryset = UserStaff.objects.all().order_by("id")
    serializer_class = StaffSerializer
    pagination_class = setPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name','phone','id')


class StaffDetails(generics.RetrieveUpdateAPIView):
    queryset = UserStaff.objects.all()
    serializer_class = UpdateStaffSerializer

class UpdateStaffDetails(generics.RetrieveUpdateAPIView):
    queryset = UserStaff.objects.all()
    serializer_class = UpdateStaffdetailsSerializer


class AddCustomer(generics.CreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CreateCutomerSerializer

class ListCustomer(generics.ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = ListCustomerSerializer




class setcusPagination(PageNumberPagination):
    page_size = 10
class paginatedCustomer(generics.ListAPIView):
    queryset = Customers.objects.all().order_by("-id")
    serializer_class = ListCustomerSerializer
    pagination_class = setcusPagination
    filter_backends = (SearchFilter,)
    search_fields = ('name','email','id','is_created','city')



class ListResponse(generics.ListAPIView):
    queryset = CustomerResponse.objects.all()
    serializer_class = ListResponseSerializer
    pagination_class = setcusPagination
    filter_backends = (SearchFilter,)
    # search_fields = ('staff')


from django.utils import timezone

class listUpcomResponce(generics.ListAPIView):
    serializer_class = ListResponseSerializer
    def get_queryset(self):
        return CustomerResponse.objects.filter(followup_to__gt=timezone.now().date())


class listCurrentResponce(generics.ListAPIView):
    serializer_class = ListResponseSerializer
    def get_queryset(self):
        return CustomerResponse.objects.filter(followup_to=datetime.now().date(),is_followed=False)



class CustomerDetails(generics.RetrieveUpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = UpdateCustomerSerializer
    def perform_update(self, serializer):
        serializer.save(updated_to=datetime.now().date())

class ListNotAsigend(generics.ListAPIView):
    queryset = Customers.objects.filter(is_asigned=False)
    serializer_class = ListCustomerSerializer

from datetime import date
class ListTodayCustomer(generics.ListAPIView):
    # now_today = datetime.now().date()
    queryset=Customers.objects.filter(is_created=date.today())
    serializer_class = ListCustomerSerializer

class InstantCustomerEdit(generics.RetrieveUpdateAPIView):
    queryset = Customers.objects.all()
    serializer_class = InstantEditSerializer

        
class AssignCustomersView(APIView):
    def post(self, request):
        user_id = request.data.get('staff')
        customer_ids = request.data.get('customer')
        asigned_by = request.data.get('asigned_by')
        try:
            user = UserStaff.objects.get(id=user_id)
            # staff = user.id
            print(user)
        except UserStaff.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        # customers = []
        # staffs = []
        for customer_id in customer_ids:
            try:
                customer = Customers.objects.get(id=customer_id)
                AssignedCustomer.objects.create(customer=customer,staff=user,asigned_by=asigned_by)
                customer.is_asigned=True
                customer.save()
                # customers.append(customer)
                # staffs.append(staff)

            except Customers.DoesNotExist:
                pass
        return Response({'message': 'Customers assigned to user successfully'}, status=status.HTTP_200_OK)
        
class AsignedCustomers(generics.ListAPIView):
    queryset = AssignedCustomer.objects.all()
    serializer_class = AsignedCustomerSerializer
            

class asigned_staff_customers(generics.ListAPIView):
    serializer_class = GetAssignedCustomerSerializer

    def get_queryset(self):
        staff_id = self.kwargs['id']
        queryset = AssignedCustomer.objects.filter(staff=staff_id)
        return queryset



@api_view(['GET'])
def get_customer(request, id):
    try:
        customer = Customers.objects.get(id=id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomerSerializer(customer)
    return Response(serializer.data)


class ListAcceptedRequst(generics.ListAPIView):
    queryset = LeaveRequest.objects.filter(is_approved=True)
    serializer_class = LeaveRequestSerializer 
    
class ListRejectedRequst(generics.ListAPIView):
    queryset = LeaveRequest.objects.filter(is_approved=False)
    serializer_class = LeaveRequestSerializer 

class ListLeaveRequst(generics.ListAPIView):
    queryset = LeaveRequest.objects.filter(is_approved=None)
    serializer_class = LeaveRequestSerializer 


# @permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_leave_request_approval(request, id):
    try:
        leave_request = LeaveRequest.objects.get(id=id)
    except LeaveRequest.DoesNotExist:
        return Response({'error': 'is_approved field is required.'},status=404)
    leave_request.is_approved = True
    leave_request.approved_by = request.user.username
    leave_request.save()
    return Response({'message': f'Leave request with id {id} has been updated.'}, status=200)



@api_view(['PUT'])
def update_leave_request_reject(request, id):
    try:
        leave_request = LeaveRequest.objects.get(id=id)
    except LeaveRequest.DoesNotExist:
        return Response({'error': 'is_approved field is required.'},status=404)
    leave_request.is_approved = False
    leave_request.approved_by = request.user.username
    leave_request.save()
    return Response({'message': f'Leave request with id {id} has been updated.'}, status=200)





@api_view(['POST'])
def update_password(request):
    user_id = request.data.get('user_id')
    new_password = request.data.get('password')
    user = UserStaff.objects.get(id=user_id)
    user.set_password(new_password)
    user.save()
    return Response({'message': 'Password updated successfully'})




from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


from datetime import datetime

# Staff_Activities_Monitoring
class SaveUserActivity(generics.CreateAPIView):
    queryset = StaffActivity.objects.all()
    serializer_class = StaffActivitySerializer

    def perform_create(self, serializer):
        serializer.validated_data['staff'] = self.request.user
        serializer.validated_data['time_at'] = datetime.now().time()
        serializer.save()


class setAcctivityPagination(PageNumberPagination):
    page_size = 15

class ListActivity(generics.ListAPIView):
    queryset = StaffActivity.objects.all().order_by('-id')
    serializer_class = ListStaffActivitySerializer
    pagination_class = setAcctivityPagination
    filter_backends = (SearchFilter,)
    search_fields = ('date_at',)






class StaffCustomerCountView(generics.ListAPIView):
    queryset = AssignedCustomer.objects.all()
    
    def get(self, request, id):
        customer_count = self.queryset.filter(staff=id).count()
        return Response(customer_count)

class StaffResponseCountView(generics.ListAPIView):
    queryset = CustomerResponse.objects.all()
    
    def get(self, request, id):
        customer_count = self.queryset.filter(staff=id).count()
        return Response(customer_count)
    

class StaffBookingCountView(generics.ListAPIView):
    queryset = BookedTours.objects.all()
    
    def get(self, request, id):
        customer_count = self.queryset.filter(staff=id).count()
        return Response(customer_count)
    

from rest_framework.parsers import MultiPartParser, FormParser
class FixedIteneariesUploadView(generics.CreateAPIView):
    serializer_class = FixedIteneariesSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)