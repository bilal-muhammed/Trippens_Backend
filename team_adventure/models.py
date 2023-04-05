from django.db import models

# Create your models here.
class TeamAdventureTour(models.Model):
    name = models.CharField(max_length=255)
    tour_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name