from rest_framework import serializers
from .models import YearlyWeatherData

class YearlyWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearlyWeatherData
        fields = '__all__'

class WeatherDataFilterSerializer(serializers.ModelSerializer):
        monthly_data = serializers.SerializerMethodField()

        class Meta:
            model = YearlyWeatherData
            fields = ['region', 'year', 'parameter', 'monthly_data']

        def get_monthly_data(self, obj):
            request = self.context.get('request')
            month = request.query_params.get('month', None) if request else None
            if month:
                month = month.lower()
                if month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']:
                    return {month: getattr(obj, month)}
            return None

class URLInputSerializer(serializers.Serializer):
    url = serializers.URLField()
