from django.shortcuts import render
from django.http import HttpResponse
from stats import (
    load_data,
    get_time_stats,
    get_station_stats,
    get_trip_duration_stats,
    get_user_stats,
    CITY_DATA,
)

def index(request):
	context = {
		'cities': [city.title() for city in CITY_DATA.keys()],
	}
	return render(request, 'dashboard/home.html', context)