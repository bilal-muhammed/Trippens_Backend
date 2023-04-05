
from rest_framework import generics
from rest_framework.views import APIView

from user_managment.models import FixedItenearies


from .serializers import *

# Create your views here.


class UserLoginRecord(generics.CreateAPIView):
    serializer_class = UserLoginRecordsSerializer

    def perform_create(self, serializer):
        serializer.save(staff=self.request.user)


# class AssignedCustomers(APIView):
    

    ##########################################################################################
    #######################################################################################

from rest_framework.decorators import api_view
from django.conf import settings
import os
from rest_framework.response import Response

# List all itenearies And DownLoading Link

@api_view(['GET'])
def fixed_itineraries_list(request):
    # retrieve all FixedItineraries objects
    fixed_itineraries = FixedItenearies.objects.all()
    
    # create a list of dictionaries with data for each object
    data_list = []
    for fi in fixed_itineraries:
        data = {'tour': fi.tour.name, 'pdf_url': fi.pdf.url, 'date': fi.date}
        data_list.append(data)
    
    # add download links to each PDF file
    for data in data_list:
        data['pdf_download'] = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, data['pdf_url']))
    
    # return the data list as a response
    return Response(data_list)