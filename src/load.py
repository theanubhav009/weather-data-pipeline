import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Read the cleaned CSV file
df = pd.read_csv("data/weather_clean.csv")

# Connect to PostgreSQL
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)


cursor = connection.cursor()

# Insert each row into PostgreSQL
for _, row in df.iterrows():
    cursor.execute(
        """
      INSERT INTO weather
(city, time, temperature, humidity, wind_speed)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (city, time) DO NOTHING
        """,
        (
            row["city"],
            row["time"],
            row["temperature"],
            row["humidity"],
            row["wind_speed"]
        )
    )

connection.commit()

cursor.close()
connection.close()

print("Weather data loaded into PostgreSQL successfully!")