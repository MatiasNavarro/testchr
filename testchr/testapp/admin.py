from django.contrib import admin

from .models import BikeStation

# Register your models here.
class BikeStationAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ("id", "name", "latitude", "longitude", "free_bikes", "empty_slots")

admin.site.register(BikeStation, BikeStationAdmin)
