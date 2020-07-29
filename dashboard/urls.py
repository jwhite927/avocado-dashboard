from django.urls import path
from . import views
from stats import CITY_DATA

urlpatterns = [
    path('', views.index, name='dashboard-home'),
    path('update/', views.update_dashboard, name='dashboard-update'),
]
