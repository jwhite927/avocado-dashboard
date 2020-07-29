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

CONTEXT = {
    'cities': CITY_DATA.keys(),
}

def index(request):
    return render(request, 'dashboard/base.html', CONTEXT)

def update_dashboard(request):
    if request.method == "POST":
        CONTEXT['city_selected'] = request.POST.get('city').title()
    return render(request, 'dashboard/home.html', CONTEXT)
