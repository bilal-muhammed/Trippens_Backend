from django.urls import path
from .views import*








urlpatterns = [


# Create,List and Update TrippensTours

    path('tours/', TourList.as_view(), name='tour-list'),
    path('tours/<int:pk>', TourDetail.as_view(), name='tour-detail'),

# List Place/Addon/Activity ..URLS..
    path('list/place', PlaceList.as_view(), name='place-list'),
    path('list/addons', AddonList.as_view(), name='addon-list'),
    path('update/addons/<int:pk>', AddonUpdate.as_view(), name='addon-update'),
    path('list/activty', ActivityList.as_view(), name='activity-list'),
    path('update/activty/<int:pk>',UpdateActivity.as_view(), name='activity-update'),

# Create New Tour Details
    path('add/place/details', AddPlace.as_view(), name='add-details'),
    path('add/tour/details', AddTourDetails.as_view(), name='add-details'),

    # path('created/tours/', CreatedTourList.as_view(), name='tour-list'),

    path('tours/place/<int:tour_id>', TourPlacesAPIView.as_view()),
    path('place/addon/<int:place_id>', PlacesAddonAPIView.as_view()),
    path('place/activity/<int:place_id>', PlacesActivityAPIView.as_view()),

    # path('get/place/<int:id>/', get_place,name="get_customer"),
# Create Tour Form
    path('create/tourform', CreateTourForm.as_view()),
    path('create/custom/itineary', AddInetenary.as_view(),),

#Customer Response
    path('customer-response/staff/<int:id>', CustomerResponseListByStaff.as_view(), name='customer-response-list-by-staff'),
    path('customer/custom/iteneary/<int:id>', CustomerForm.as_view(), name='customers-custom-itenearies'),

]