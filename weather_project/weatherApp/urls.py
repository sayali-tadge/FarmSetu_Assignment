from django.urls import path
from .views import YearlyWeatherDataList, YearlyWeatherDataDetail, WeatherDataAPI , WeatherDataFilterViewSet, filter_view

urlpatterns = [
    path('parse-weather-data/', WeatherDataAPI.as_view(), name='parse-weather-data'),
    path('weather/', YearlyWeatherDataList.as_view(), name='weather-list'),
    path('weather/<int:pk>/', YearlyWeatherDataDetail.as_view(), name='weather-detail'),
    path('weatherdatafilter/', WeatherDataFilterViewSet.as_view({'get': 'list'}), name='weatherdata-filter'),
    path('filter/', filter_view, name='filter-view'),
]
