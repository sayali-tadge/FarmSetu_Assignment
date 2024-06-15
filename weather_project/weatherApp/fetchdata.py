import requests
from .models import WeatherData

def fetch_weather_data():
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Rainfall/ranked/Scotland.txt"
    response = requests.get(url)
    lines = response.text.splitlines()

    # Skip the header lines
    data_lines = lines[7:]

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
        WeatherData.objects.update_or_create(year=year, defaults=data)
