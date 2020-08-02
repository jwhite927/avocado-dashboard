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
    'cities': CITY_DATA.keys(),
    'city_selected': 'Chicago',
    'months': MONTHS,
}

class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/home.html', CONTEXT)

    def post(self, request):
        print(request.POST)
        CONTEXT['city_selected'] = request.POST.get('city')
        return JsonResponse({'city_selected': CONTEXT['city_selected']}, status=200)
        # return JsonResponse({'city_selected': CONTEXT['city_selected']}, status=200)
