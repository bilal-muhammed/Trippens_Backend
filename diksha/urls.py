from django.urls import path
from .views import*








urlpatterns = [


# Create,List and Update DikshaTours
    path('tours/', TourList.as_view(), name='tour-list'),
    path('tours/<int:pk>/', TourDetail.as_view(), name='tour-detail'),


    
]