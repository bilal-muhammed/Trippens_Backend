from django.urls import path
from .views import*


urlpatterns = [

    path('list/download/Itinearies', fixed_itineraries_list,name="list_fixed"),

    path('user-login-records/',UserLoginRecord.as_view(), name='user-login-records'),



]