from django.db import models

# Create your models here.



class BusStopTime(models.Model):
    bus_stop = models.OneToOneField("geography.BusStop", on_delete=models.CASCADE)
    time = models.TimeField()

class BusShift(models.Model):
    bus = models.ForeignKey("fleet.Bus", on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey("fleet.Driver", on_delete=models.SET_NULL, null=True)
    bus_stops_times = models.ManyToManyField(BusStopTime)
    bus_shift = models.Manager()

    
