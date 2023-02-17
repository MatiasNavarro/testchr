from django.urls import path
from . import views

urlpatterns = [
    path('get-data-from-sea/', views.get_data_from_sea, name='get_data_from_sea'),
    path('show-sea-projects/', views.show_sea_projects, name='show_sea_projects'),
]
