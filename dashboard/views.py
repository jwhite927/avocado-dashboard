from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

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
    'cities': {"chicago": {"pretty": "Chicago", "selected": True}, "newyork": {"pretty": "New York City", "selected": False}, "washington": {"pretty": "Washington D.C.", "selected": False} },
    'months': MONTHS,
}

def reset_cities(context):
    for city, props in context['cities'].items():
        props['selected'] = False

class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/home.html', CONTEXT)

    def post(self, request):
        global CONTEXT
        reset_cities(CONTEXT)
        info = {'city_selected': ''}
        for key in request.POST.keys():
            for city, props in CONTEXT['cities'].items():
                if key == f'city-{city}':
                    props['selected'] = True
                    info['city_selected'] += city

        return JsonResponse(info, status=200)
