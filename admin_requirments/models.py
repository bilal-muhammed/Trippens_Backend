from django.db import models
from trippens.models import *

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name



class Branches(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    address = models.TextField()
    is_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    place = models.ForeignKey(TrippensTour,on_delete=models.CASCADE) 
    name = models.CharField('Vehicle Name',max_length=50)
    category = models.CharField(max_length=20)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name
    

class Rooms(models.Model):

    place = models.ForeignKey(TrippensTour,on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    category = models.CharField('Room Category',max_length=20)
    price = models.FloatField('Room Price/Day',null=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Designation(models.Model):
    designation = models.CharField(max_length=30,null=False)
    designation_id = models.CharField(max_length=10)

    def __str__(self):
        return self.designation
    






from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, address, branch, phone, designation, adhar_no, profile_pic, image, username, name, password=None,):
       
        
        if not username:
            raise ValueError('User must have an Username')

        user = self.model(
            
            username    = username,
            name        = name,
            phone       = phone,
            address     = address,
            branch      = branch,
            designation = designation,
            adhar_no    = adhar_no,
            profile_pic = profile_pic,
            image       = image
            
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, username,  password):
        user = self.create_user(
            # email      = self.normalize_email(email),
            username   = username,
            password   = password,
            
        )
        
        user.is_admin   = True
        user.is_active  = True
        user.is_staff   = True
        user.is_superadmin  = True
        user.save(using=self._db)
        return user
    

class UserStaff(AbstractBaseUser):
    name            = models.CharField(max_length=50,null=True)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100,blank=True)
    phone           = models.CharField(max_length=50,null=True)
    last_login      = models.DateTimeField(auto_now_add=True)  
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    address         = models.TextField(blank=True,null=True)    
    branch          = models.ForeignKey(Branches,on_delete=models.CASCADE,blank=True,null=True)
    designation     = models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)
    adhar_no        = models.CharField(max_length=20,blank=True)
    profile_pic     = models.ImageField(upload_to='media/staff_images/', blank=True, null=True)
    image           = models.ImageField(upload_to='media/staff_credentials/', blank=True, null=True)
    last_logout     = models.DateTimeField(null=True)
    
    USERNAME_FIELD      = 'username'
    REQUIRED_FIELDS     = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    


class TourForm(models.Model):
    from user_managment.models import Customers

    customer = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True)
    tour_date = models.DateField()
    days_count = models.IntegerField()
    night_count = models.IntegerField()
    adult_count = models.IntegerField()
    child_count = models.IntegerField(default=0)
    pick_up = models.CharField(max_length=100)
    drop_off = models.CharField(max_length=100)
    rooms = models.ForeignKey(Rooms,on_delete=models.SET_NULL,null=True)
    vehicles = models.ForeignKey(Vehicle,on_delete=models.SET_NULL,null=True)
    remarks = models.TextField(max_length=200,blank=True)
    include = models.TextField(max_length=200,blank=True)
    exclude = models.TextField(max_length=200,blank=True)
    expired_at = models.DateField()
    created_at = models.DateField(auto_now_add=True)



class CustomInetenary(models.Model):
    form_id = models.ForeignKey(TourForm,on_delete=models.CASCADE)
    day = models.IntegerField()
    tour = models.ForeignKey(TrippensTour,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    addon = models.ManyToManyField(Addon, related_name='customInetenary', blank=True)
    activivty = models.ManyToManyField(Activity, related_name='customInetenary', blank=True)


class Accounts(models.Model):
    from user_managment.models import Customers
    date = models.DateField(auto_now_add=True)
    form_id = models.ForeignKey(TourForm,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True)
    staff = models.ForeignKey(UserStaff,on_delete=models.SET_NULL,null=True)
    total = models.FloatField() 
    gst = models.IntegerField(default=5) 
    offer = models.FloatField(default=0) 
    extra_amount = models.IntegerField(default=0)
    is_done = models.BooleanField(default=False)
    is_veryfied = models.CharField(max_length=100,blank=True)




class BookedTours(models.Model):
    from user_managment.models import Customers
    date = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    customer = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True)
    staff = models.ForeignKey(UserStaff,on_delete=models.SET_NULL,null=True)
    accounts = models.ForeignKey(Accounts,on_delete=models.SET_NULL,null=True)
    payment_status = models.CharField(max_length=100,default="Pending")
    total = models.FloatField(blank=True)  

    


class Transacions(models.Model):
    bookedtours = models.ForeignKey(BookedTours,on_delete=models.SET_NULL,null=True)

    trans_id = models.CharField(max_length=100,blank=True)
    Advance = models.FloatField(blank=True)
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=100,blank=True)

