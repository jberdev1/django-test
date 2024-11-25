from django.db import models
from django.conf import settings

class Place(models.Model):
    name = models.CharField("Name of the place", max_length=50)

    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6)
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6)

    class Meta:
        # Two places cannot be located at the same coordinates.
        unique_together = (("longitude", "latitude"), )

    def __str__(self):
        return f"Place: {self.name} (id: {self.pk})"

class BusStop(models.Model):
    name = models.CharField("Name of the bus stop", max_length=50)

    bus_stop = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='bus_stop')

    class Meta:
        # Two bus stops cannot have the same name
        unique_together = (("name"),)

    def __str__(self):
        return f"Bus stop: {self.name} (id: {self.pk})"

