import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import BikeStation


# Create your views here.
def bike_info(request):
    response = requests.get('http://api.citybik.es/v2/networks/bikesantiago')
    data = response.json()
    return render(request, 'testapp/bike_info.html', {
        'data': data
    })

def update_bike_stations(request):
    url = 'http://api.citybik.es/v2/networks/bikesantiago'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['network']['stations']
        for station in data:
            uuid = station['id']
            name = station['name']
            empty_slots = int(station['empty_slots'])
            free_bikes = int(station['free_bikes'])
            latitude = float(station['latitude'])
            longitude = float(station['longitude'])
            timestamp = station['timestamp']
            address = station['extra']['address']
            altitude = float(station['extra']['altitude'])
            ebikes = int(station['extra']['ebikes'])
            has_ebikes = station['extra']['has_ebikes']
            last_updated = int(station['extra']['last_updated'])
            normal_bikes = int(station['extra']['normal_bikes'])
            payment = station['extra']['payment']
            payment_terminal = station['extra']['payment-terminal']
            if 'post_code' in station['extra']:
                post_code = station['extra']['post_code']
            else: 
                post_code = ''
            renting = int(station['extra']['renting'])
            returning = int(station['extra']['returning'])
            slots = int(station['extra']['slots'])
            uid = station['extra']['uid']
            BikeStation.objects.update_or_create(
                uuid=uuid,
                defaults={
                    'name': name,
                    'empty_slots': empty_slots,
                    'free_bikes': free_bikes,
                    'latitude': latitude,
                    'longitude': longitude,
                    'timestamp': timestamp,
                    'address': address,
                    'altitude': altitude,
                    'ebikes': ebikes,
                    'has_ebikes': has_ebikes,
                    'last_updated': last_updated,
                    'normal_bikes': normal_bikes,
                    'payment': payment,
                    'payment_terminal': payment_terminal,
                    'post_code': post_code,
                    'renting': renting,
                    'returning': returning,
                    'slots': slots,
                    'uid': uid
                }
            )
        return HttpResponse('Bike stations updated successfully')
    else:
        return HttpResponse('Unable to update bike stations')


def show_bike_stations(request):
    bike_stations = BikeStation.objects.all()
    return render(request, 'testapp/show_bike_stations.html', {'bike_stations': bike_stations})