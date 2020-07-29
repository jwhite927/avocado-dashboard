from django.urls import path
from . import views
from stats import CITY_DATA

urlpatterns = [
    path('', views.index, name='dashboard-home'),
    path('update-city/', views.update_city, name='dashboard-update-city'),
    path('update-month/', views.update_month, name='dashboard-update-month'),
]
