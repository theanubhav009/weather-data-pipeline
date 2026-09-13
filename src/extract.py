import requests
import json
from datetime import datetime

cities = {
    "Indore": (22.7196, 75.8577),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.6139, 77.2090),
    "Bengaluru": (12.9716, 77.5946),
    "Pune": (18.5204, 73.8567)
}

weather_data = []

date = datetime.now().strftime("%Y-%m-%d")

for city, (latitude, longitude) in cities.items():

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={date}&end_date={date}"
        f"&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&timezone=Asia%2FKolkata"
    )

    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    weather_data.append({
        "city": city,
        "data": data
    })

with open("data/raw/weather.json", "w") as file:
    json.dump(weather_data, file, indent=4)

print("Historical weather data saved successfully!")