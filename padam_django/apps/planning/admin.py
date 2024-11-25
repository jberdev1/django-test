from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    pass

@admin.register(models.BusStopTime)
class BusStopTimeAdmin(admin.ModelAdmin):
    pass


