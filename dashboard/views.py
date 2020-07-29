from django.shortcuts import render
from django.http import HttpResponse
from stats import (
    load_data,
    get_time_stats,
    get_station_stats,
    get_trip_duration_stats,
    get_user_stats,
    CITY_DATA,
    MONTHS,
)

CONTEXT = {
    'cities': CITY_DATA.keys(),
    'city_selected': 'Chicago',
    'months': MONTHS,
}

def index(request):
    return render(request, 'dashboard/base.html', CONTEXT)

def update_city(request):
    if request.method == "POST":
        CONTEXT['city_selected'] = request.POST.get('city')
    return render(request, 'dashboard/base.html', CONTEXT)

def update_month(request):
    if request.method == "POST":
        month = request.POST.get('month')
        CONTEXT['months'][month] = not CONTEXT['months'][month]
    return render(request, 'dashboard/base.html', CONTEXT)

