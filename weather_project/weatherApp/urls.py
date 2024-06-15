# weather/urls.py
from django.urls import path
from .views import YearlyWeatherDataListCreate, YearlyWeatherDataDetail, WeatherDataAPI

urlpatterns = [
    path('weather/', YearlyWeatherDataListCreate.as_view(), name='weather-list-create'),
    path('weather/<int:pk>/', YearlyWeatherDataDetail.as_view(), name='weather-detail'),
    path('parse-weather-data/', WeatherDataAPI.as_view(), name='parse-weather-data'),
]
