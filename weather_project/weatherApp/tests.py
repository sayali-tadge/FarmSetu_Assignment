from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import YearlyWeatherData

class WeatherDataModelTestCase(TestCase):
    def setUp(self):
        YearlyWeatherData.objects.create(year=2020, region='Scotland', parameter='Rainfall', jan=10.0)

    def test_model_str(self):
        data = YearlyWeatherData.objects.get(year=2020)
        self.assertEqual(str(data), 'Scotland Rainfall 2020')

class WeatherDataAPITestCase(APITestCase):
    def setUp(self):
        YearlyWeatherData.objects.create(year=2020, region='Scotland', parameter='Rainfall', jan=10.0)

    def test_get_weather_data(self):
        url = reverse('weather-list')
        response = self.client.get(url, {'region': 'Scotland', 'parameter': 'Rainfall', 'year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # def test_filter_by_month(self):
    #     url = reverse('weatherdata-filter')
    #     response = self.client.get(url, {'region': 'Scotland', 'parameter': 'Rainfall', 'year': 2020, 'month': 'jan'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data[0]['jan'], 10.0)
