# weather/serializers.py
from rest_framework import serializers
from .models import YearlyWeatherData

class YearlyWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyWeatherData
        fields = '__all__'

class URLInputSerializer(serializers.Serializer):
    url = serializers.URLField()
