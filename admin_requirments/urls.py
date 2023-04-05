from django.urls import path, include
from rest_framework import routers
from .views import*

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),

# Create,List and Update Branches 
    path('list/branches',BranchListAPIView.as_view(),name='branch-list'),
    path('create/branches',BranchCreateAPIView.as_view(),name='branch-list'),
    path('branches/update/<int:pk>',BranchRetrieveUpdateAPIView.as_view(),name='branch-update'),

# Create,List and Update Vehicle 
    path('create/vehicles',VehicleListCreateAPIView.as_view(),name='vehile-create'),
    path('list/vehicles',VehicleListAPIView.as_view(),name='vehile-list'),
    path('vehicles/update/<int:pk>',VehicleRetriveUpdateAPIView.as_view(),name='vehicle-update'),

# Create,List and Update Rooms
    path('create/rooms',RoomCreateAPIView.as_view(),name='rooms-list'),
    path('list/rooms',RoomListAPIView.as_view(),name='rooms-list'),
    path('rooms/update/<int:pk>',RoomRetriveUpdateAPIView.as_view(),name='rooms-update'),

# Create,List and Update Designatios
    path('designations/', DesignationList.as_view(), name='designation-list'),
    path('designations/<int:pk>/', DesignationDetail.as_view(), name='designation-detail'),

    

# Admin Dashboard ...!

    path('customer/counts', Customer_counts, name='update_password'),
    path('booking/counts', Booking_count, name='update_password'),
    path('followups/counts', Followups_count, name='update_password'),


# View Inteneary

    path('custom_itinerary/<int:id>', CustomInetenaryList.as_view()),
    path('tour_form/<int:pk>', TourFormDetails.as_view()),

# Add_Bookings to Accounts
    path('add/to/accounts', AddAcounts.as_view(), name='add/to/accounts'),
    path('list/accounts', ListAccounts.as_view(), name='list_accounts'),
    path('list/completed/accounts', ListAccountsCompleted.as_view(), name='list_completed_accounts'),
    path('verfy/accounts/<int:pk>', VerifyAccounts.as_view(), name='list_accounts'),
    path('update/accounts/<int:pk>', UpdateAccounts.as_view(), name='list_accounts'),

# Confirm Bookings..!


    path('confirm/booking', Create_booked_tour, name='confirm_booking'),
# List Booked Serializer..!

    path('List/bookings', ListBookedTours.as_view(), name='list_accounts'),
    path('List/confirm/bookings', ListConfirmedTours.as_view(), name='list_confirm_accounts'),
    path('get/booked/tour/<int:pk>', GetBookedTour.as_view(), name='list_accounts'),
    path('get/advance/tour/<int:pk>', AddAdvance.as_view(), name='list_accounts'),
    
# Create Trsnsactions and List transaction realed bill

    path('add/transaction', AddTransation.as_view(), name='add_transaction'),
    path('list/transaction/<int:id>', ListTransactions.as_view(), name='list_accounts'),




]




    