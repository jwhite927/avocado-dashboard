from django.urls import path
from .views import Dashboard
from stats import CITY_DATA

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard-home'),
]
