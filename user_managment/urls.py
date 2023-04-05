from django.urls import path
from .views import*
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    # TokenVerifyView
)


urlpatterns = [
# Add Fixed Itineary PDF'S


    path('fixed-itineraries/upload/',FixedIteneariesUploadView.as_view(),name='list_staffs'),



# List,Create,Update and Delete Staff 
    path('add/staff',UserRegistrationView.as_view(),name='add_new_staff'),
    path('list/staffs',paginatedStaff.as_view(),name='list_staffs'),
    path('listall/staffs',ListStaff.as_view(),name='list_staffs'),
    path('staff/details/<int:pk>',StaffDetails.as_view(),name='list_staffs'),
    path('staff/update/<int:pk>',Updatestaff.as_view(),name='list_staffs'),
    path('staff/details/update/<int:pk>',UpdateStaffDetails.as_view(),name='update_staffs_details'),
# Update Password Only
    path('update/password', update_password, name='update_password'),

# List,Create,Update and Delete Customers 
    path('add/customer',AddCustomer.as_view(),name='add_new_customer'),
    path('list/customer',ListCustomer.as_view(),name='list_all_customer'),
    path('list/todays/customer',ListTodayCustomer.as_view(),name='list_now_customer'),
    path('customer/details/<int:pk>',CustomerDetails.as_view(),name='customer_details'),
    path('customer/instentedit/<int:pk>',InstantCustomerEdit.as_view(),name='customer_instant_edit'),

    path('paginated/customer',paginatedCustomer.as_view(),name='list_all_customer'),



# List All Customer Respose With Pagunation

    path('response/customer',ListResponse.as_view(),name='list_all_response'),
    path('Upcoming/response/customer',listUpcomResponce.as_view(),name='list_all_response'),
    path('current/response/customer',listCurrentResponce.as_view(),name='list_all_response'),
 



# Not Asigned Customer
    path('list/not/asigned',ListNotAsigend.as_view(),name='list_not_asigned_customer'),

# Assign Customer to Staffs
    path('asign/customer', AssignCustomersView.as_view(), name='ajhgahjg'),
    path('asigned/customers', AsignedCustomers.as_view(), name='ajhgahjg'),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),

    path('check-username/<str:username>/', check_username,name="check_username"),

#Leave Request List\Create 

    path('leave/requests', ListLeaveRequst.as_view(), name='all_leaves'),
    path('accepted/requests', ListAcceptedRequst.as_view(), name='accepted_leaves'),
    path('rejected/requests', ListRejectedRequst.as_view(), name='rejected_leaves'),
    path('accept/request/<int:id>', update_leave_request_approval,name="approve_request"),
    path('reject/request/<int:id>', update_leave_request_reject,name="approve_request"),


# Search Customer With Id
    path('get/customer/<int:id>', get_customer,name="get_customer"),
    path('get/staff/customer/<int:id>',asigned_staff_customers.as_view(),name="get_staff_assigned_customer"),

# api test
    path('test/', testEndPoint, name='test'),

# User_Activity Saving..

    path('save/activity', SaveUserActivity.as_view(), name='save_user_activity'),
    path('list/activity', ListActivity.as_view(), name='list_user_activity'),

# Staff assigned booking counts and agregations
    path('staff/customer/<int:id>', StaffCustomerCountView.as_view(), name='list_user_activity'),
    path('staff/response/<int:id>', StaffResponseCountView.as_view(), name='list_user_activity'),
    path('staff/bookings/<int:id>', StaffBookingCountView.as_view(), name='list_user_activity'),



]
