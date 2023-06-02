import requests
import json
import sys

def get_weather(city_name):
    api_key = "b9356312f2b2218c69a1213ea9cd2ea2" 
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {

        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Use Copilot to suggest accessing nested data and handling potential errors
        weather_description = weather_data.get("weather", [{}])[0].get("description")
        temperature = weather_data.get("main", {}).get("temp")
        humidity = weather_data.get("main", {}).get("humidity")
        wind_speed = weather_data.get("wind", {}).get("speed")

        # Printing the weather forecast
        print(f"Weather forecast for {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        sys.exit(1)

    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        sys.exit(1)

    except KeyError as err:
        print(f"Error parsing weather data: {err}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a city name as an argument.")
        sys.exit(1)

    city_name = sys.argv[1]
    get_weather(city_name)
