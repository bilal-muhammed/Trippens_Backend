from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import*
from .serializers import TeamAdvTourSerializer

class TourList(generics.ListCreateAPIView):
    queryset = TeamAdventureTour.objects.all()
    serializer_class = TeamAdvTourSerializer

class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamAdventureTour.objects.all()
    serializer_class = TeamAdvTourSerializer


