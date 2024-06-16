# weather/urls.py
from django.urls import path
from .views import YearlyWeatherDataList, YearlyWeatherDataDetail, WeatherDataAPI , WeatherDataViewSet, filter_view

urlpatterns = [
    path('weather/', YearlyWeatherDataList.as_view(), name='weather-list'),
    path('weather/<int:pk>/', YearlyWeatherDataDetail.as_view(), name='weather-detail'),
    path('weatherdataFilter/', WeatherDataViewSet.as_view({'get': 'list'}), name='weatherdata-filter'),
    path('parse-weather-data/', WeatherDataAPI.as_view(), name='parse-weather-data'),
    path('filter/', filter_view, name='filter-view'),
]
