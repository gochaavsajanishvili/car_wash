from django.contrib import admin
from .models import CarWash, Garage, WashPrice, WashType, Washer, Location


class GarageTabularInline(admin.TabularInline):
    model = Garage


class CarWashAdmin(admin.ModelAdmin):
    inlines = [GarageTabularInline]

    class Meta:
        model = CarWash


admin.site.register(CarWash, CarWashAdmin)

admin.site.register([Garage, WashPrice, WashType, Washer, Location])
