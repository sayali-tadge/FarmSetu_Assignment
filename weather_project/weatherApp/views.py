# weather/views.py
import requests
import pandas as pd
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import YearlyWeatherData
from .serializers import YearlyWeatherDataSerializer, URLInputSerializer
import re
import csv

class YearlyWeatherDataListCreate(generics.ListCreateAPIView):
    queryset = YearlyWeatherData.objects.all()
    serializer_class = YearlyWeatherDataSerializer

class YearlyWeatherDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = YearlyWeatherData.objects.all()
    serializer_class = YearlyWeatherDataSerializer


class WeatherDataAPI(APIView):
    def post(self, request):
        region = request.data.get('region')
        parameter = request.data.get('parameter')
        url = request.data.get('url', '')
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            
            lines = response.text.splitlines()
            data_lines = lines[7:]  # Skip header lines
            
            for line in data_lines:
                values = line.split()
                if len(values) < 18:
                    continue  # Skip lines that don't have enough data
                
                year = int(values[0])
                data = {
                    'year': year,
                    'jan': float(values[1]),
                    'feb': float(values[2]),
                    'mar': float(values[3]),
                    'apr': float(values[4]),
                    'may': float(values[5]),
                    'jun': float(values[6]),
                    'jul': float(values[7]),
                    'aug': float(values[8]),
                    'sep': float(values[9]),
                    'oct': float(values[10]),
                    'nov': float(values[11]),
                    'dec': float(values[12]),
                    'win': float(values[13]),
                    'spr': float(values[14]),
                    'sum': float(values[15]),
                    'aut': float(values[16]),
                    'ann': float(values[17]),
                }
                
                # Update or create WeatherData object
                YearlyWeatherData.objects.update_or_create(region=region,
                                                        parameter=parameter,
                                                        year=year, 
                                                        defaults=data)
            
            return Response({'message': 'Data saved successfully'})
        
        except requests.exceptions.RequestException as e:
            return Response({'error': f'Failed to fetch data from URL: {url}. Error: {str(e)}'}, status=400)








