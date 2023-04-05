from django.shortcuts import render
from .models import*
from rest_framework import generics
from .serializers import*


# Create your views here.
class TourList(generics.ListCreateAPIView):
    queryset = DikshaTour.objects.all()
    serializer_class = DikshaTourSerializer

class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DikshaTour.objects.all()
    serializer_class = DikshaTourSerializer