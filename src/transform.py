import json
import pandas as pd

with open("data/raw/weather.json", "r") as file:
    data = json.load(file)

weather_rows = []

for city_data in data:

    city = city_data["city"]
    hourly = city_data["data"]["hourly"]

    for i in range(len(hourly["time"])):

        weather_rows.append({
            "city": city,
            "time": hourly["time"][i],
            "temperature": hourly["temperature_2m"][i],
            "humidity": hourly["relative_humidity_2m"][i],
            "wind_speed": hourly["wind_speed_10m"][i]
        })

df = pd.DataFrame(weather_rows)

print(df)
print(f"\nTotal records: {len(df)}")

df.to_csv("data/weather_clean.csv", index=False)

print("Historical weather data transformed successfully!")