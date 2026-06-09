import requests
from datetime import datetime, timezone

API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=572a261038383772a579db89e5f86af3&units=metric"


def format_time(unix_time, tz_offset_seconds):
    if unix_time is None:
        return "N/A"
    return datetime.fromtimestamp(unix_time + tz_offset_seconds, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def weather_data(city):
    url = API_URL.format(city=city)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        wind = data.get("wind", {})
        sys_data = data.get("sys", {})
        coord = data.get("coord", {})
        clouds = data.get("clouds", {})
        timezone_offset = data.get("timezone", 0)

        print("City:", data.get("name", city))
        print("Country:", sys_data.get("country", "N/A"))
        print("Latitude:", coord.get("lat", "N/A"))
        print("Longitude:", coord.get("lon", "N/A"))
        print("Weather:", weather.get("main", "N/A"))
        print("Description:", weather.get("description", "N/A"))
        print("Temperature:", main.get("temp", "N/A"))
        print("Feels Like:", main.get("feels_like", "N/A"))
        print("Minimum Temperature:", main.get("temp_min", "N/A"))
        print("Maximum Temperature:", main.get("temp_max", "N/A"))
        print("Humidity:", main.get("humidity", "N/A"))
        print("Pressure:", main.get("pressure", "N/A"))
        print("Wind Speed:", wind.get("speed", "N/A"))
        print("Wind Direction:", wind.get("deg", "N/A"))
        print("Cloudiness:", clouds.get("all", "N/A"))
        print("Visibility:", data.get("visibility", "N/A"))
        print("Sunrise:", format_time(sys_data.get("sunrise"), timezone_offset))
        print("Sunset:", format_time(sys_data.get("sunset"), timezone_offset))
    except requests.exceptions.RequestException as e:
        print("Unable to fetch weather data:", e)


city = input("Enter city name: ")
weather_data(city)
