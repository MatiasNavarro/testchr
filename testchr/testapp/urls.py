from django.urls import path
from . import views

urlpatterns = [
    path("bike-info/", views.bike_info, name="bike_info"),
    path('update-bike-stations/', views.update_bike_stations, name='update_bike_stations'),
    path('show-bike-stations/', views.show_bike_stations, name='show_bike_stations'),
]