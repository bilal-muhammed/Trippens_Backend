from django.db import models
from trippens.models import TrippensTour
from admin_requirments.models import Branches

# Create your models here.

class Customers(models.Model):

    name        = models.CharField(max_length=20)
    email       = models.EmailField(blank=True)
    is_created  = models.DateField(auto_now_add=True)
    updated_to  = models.DateField(null=True)
    phone       = models.CharField(max_length=12)
    address     = models.TextField(blank=True)
    whatsapp    = models.CharField('Whatsapp Number',max_length=12,blank=True)
    city        = models.CharField(max_length=50,null=True)
    pax         = models.IntegerField(null=True)
    category    = models.CharField(max_length=50,blank=True)
    tours        = models.ForeignKey(TrippensTour,on_delete=models.CASCADE)
    branch      = models.ForeignKey(Branches,on_delete=models.CASCADE,null=True)
    type        = models.CharField(max_length=50,blank=True)
    vehicle     = models.CharField(max_length=50,blank=True)
    progress    = models.CharField(max_length=50,blank=True)
    source      = models.CharField(max_length=50,null=True)
    remarks     = models.TextField(blank=True)
    is_asigned  = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    


class AssignedCustomer(models.Model):
    from admin_requirments.models import UserStaff

    staff = models.ForeignKey(UserStaff,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    progress = models.CharField(max_length=50)
    attented = models.BooleanField(default=False)
    asigned_by = models.CharField(max_length=100,blank=True)
    date = models.DateField(auto_now_add=True)




    
class CustomerResponse(models.Model):
    from admin_requirments.models import UserStaff
    staff = models.ForeignKey(UserStaff,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    reply = models.TextField(max_length=300)
    response  = models.TextField(max_length=300)
    date  = models.DateField(auto_now_add=True)
    followup_to = models.DateField()
    followup_time   = models.TimeField()
    is_followed = models.BooleanField(default=False)



class LeaveRequest(models.Model):
    from admin_requirments.models import UserStaff

    staff = models.ForeignKey(UserStaff,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)
    reason = models.TextField(max_length=300,null=False)
    date_from = models.DateField()
    date_to = models.DateField()
    is_approved = models.BooleanField(null=True)
    approved_by = models.CharField(max_length=50)
 
    
class StaffActivity(models.Model):
    from admin_requirments.models import UserStaff
    staff = models.ForeignKey(UserStaff,on_delete=models.SET_NULL,null=True)
    date_at = models.DateField(auto_now_add=True)
    activity = models.CharField(max_length=350,null=False)
    time_at = models.TimeField()



class Audio(models.Model):
    response = models.ForeignKey(CustomerResponse,on_delete=models.SET_NULL,null=True)
    date = models.DateField(auto_now_add=True)
    audio_file = models.FileField(upload_to='audio_files/')


class FixedItenearies(models.Model):
    tour = models.ForeignKey(TrippensTour,on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='fixed_itineary/')
    date = models.DateField(auto_now_add=True)

