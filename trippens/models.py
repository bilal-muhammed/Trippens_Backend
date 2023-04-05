from django.db import models



# Create your models here.
class TrippensTour(models.Model):
    name = models.CharField(max_length=255)
    tour_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name




class Place(models.Model):
    tour = models.ForeignKey(TrippensTour,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    # def __str__(self):
    #     return self.name


class Addon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    price = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.name
    

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    price = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.name
    




