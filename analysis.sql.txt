-- 1. Average temperature by city
SELECT
    city,
    ROUND(AVG(temperature), 2) AS avg_temperature
FROM weather
GROUP BY city
ORDER BY avg_temperature DESC;


-- 2. Average humidity by city
SELECT
    city,
    ROUND(AVG(humidity), 2) AS avg_humidity
FROM weather
GROUP BY city
ORDER BY avg_humidity DESC;


-- 3. Highest temperature recorded
SELECT
    city,
    MAX(temperature) AS highest_temperature
FROM weather
GROUP BY city
ORDER BY highest_temperature DESC;


-- 4. Lowest temperature recorded
SELECT
    city,
    MIN(temperature) AS lowest_temperature
FROM weather
GROUP BY city
ORDER BY lowest_temperature ASC;


-- 5. Hourly weather for Indore
SELECT
    time,
    temperature,
    humidity,
    wind_speed
FROM weather
WHERE city = 'Indore'
ORDER BY time;