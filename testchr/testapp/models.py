from django.db import models

# Create your models here.
class BikeStation(models.Model):
    uuid = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
    address = models.CharField(max_length=200)
    altitude = models.FloatField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payment = models.JSONField()
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=10)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.name}"