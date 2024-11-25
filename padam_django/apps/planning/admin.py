from django.contrib import admin
from . import models
from django.db.models import Value, TimeField
from django import forms



class BusShiftForm(forms.ModelForm):
    class Meta:
        model = models.BusShift
        exclude=[]

    def clean(self):
        print(self.data)
        return super().clean()


# Register your models here.
@admin.register(models.BusShift)
class BusShiftAdmin(admin.ModelAdmin):

    form = BusShiftForm

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        times = qs.values("bus_stops_times__time").order_by("bus_stops_times__time")
        start_time = times.first()
        end_time = times.last()
        print(start_time)
        end_time = qs.values_list().order_by("bus_stops_times__time").last()
        return qs


@admin.register(models.BusStopTime)
class BusStopTimeAdmin(admin.ModelAdmin):
    pass


