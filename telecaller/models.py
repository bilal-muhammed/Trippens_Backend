from django.db import models

from admin_requirments.models import UserStaff
# Create your models here.
class UserLoginRecords(models.Model):
    staff = models.ForeignKey(UserStaff,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()


class UserLogOutRecords(models.Model):
    staff = models.ForeignKey(UserStaff,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()

