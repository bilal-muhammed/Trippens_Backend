from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import*
from .serializers import GossipTourSerializer

class TourList(generics.ListCreateAPIView):
    queryset = GossipTour.objects.all()
    serializer_class = GossipTourSerializer

class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GossipTour.objects.all()
    serializer_class = GossipTourSerializer