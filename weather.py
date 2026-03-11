"""
Weather Forecast CLI Tool
Author: Logesh T
Description: CLI app that fetches real-time weather data using OpenWeatherMap REST API
"""

import sys

try:
    import requests
except ImportError:
    print("Error: 'requests' module is not installed. Please install it using: pip install requests")
    sys.exit(1)

import json

API_KEY = "7a83771608905d86e9c213dff8cdb2d8"  # Replace with your own valid API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> dict:
    """
    Fetch weather data for a given city using OpenWeatherMap REST API.

    Args:
        city (str): Name of the city

    Returns:
        dict: Parsed JSON weather data

    Raises:
        ValueError: If city is not found or API key is invalid
        ConnectionError: If network request fails
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 401:
            raise ValueError("Invalid API key. Please check your OpenWeatherMap API key.")

        if response.status_code == 404:
            raise ValueError(f"City '{city}' not found. Please check the city name and try again.")

        if response.status_code != 200:
            raise ConnectionError(f"API request failed with status code {response.status_code}")

        return response.json()

    except requests.exceptions.ConnectionError:
        raise ConnectionError("Network error: Unable to reach the OpenWeatherMap API. Check your internet connection.")

    except requests.exceptions.Timeout:
        raise ConnectionError("Request timed out. Please try again later.")

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Unexpected network error: {e}")


def parse_weather(data: dict) -> dict:
    """
    Parse and extract key weather fields from raw API JSON response.

    Args:
        data (dict): Raw JSON response from OpenWeatherMap API

    Returns:
        dict: Cleaned and structured weather data
    """
    return {
        "city": data.get("name", "Unknown"),
        "country": data.get("sys", {}).get("country", "N/A"),
        "temperature": data.get("main", {}).get("temp", "N/A"),
        "feels_like": data.get("main", {}).get("feels_like", "N/A"),
        "humidity": data.get("main", {}).get("humidity", "N/A"),
        "pressure": data.get("main", {}).get("pressure", "N/A"),
        "weather": data.get("weather", [{}])[0].get("description", "N/A").capitalize(),
        "wind_speed": data.get("wind", {}).get("speed", "N/A"),
        "visibility": data.get("visibility", "N/A")
    }


def display_weather(weather: dict) -> None:
    """
    Display formatted weather information in the CLI.

    Args:
        weather (dict): Parsed weather data
    """
    print("\n" + "=" * 45)
    print(f"  Weather Report: {weather['city']}, {weather['country']}")
    print("=" * 45)
    print(f"  Condition     : {weather['weather']}")
    print(f"  Temperature   : {weather['temperature']}°C (Feels like {weather['feels_like']}°C)")
    print(f"  Humidity      : {weather['humidity']}%")
    print(f"  Pressure      : {weather['pressure']} hPa")
    print(f"  Wind Speed    : {weather['wind_speed']} m/s")
    print(f"  Visibility    : {weather['visibility']} m" if weather['visibility'] != 'N/A' else "  Visibility    : N/A")
    print("=" * 45 + "\n")


def main():
    """Main entry point for the CLI application."""
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        sys.exit(1)

    try:
        raw_data = get_weather(city)
        weather = parse_weather(raw_data)
        display_weather(weather)

    except ValueError as e:
        print(f"\nInput Error: {e}\n")
        sys.exit(1)

    except ConnectionError as e:
        print(f"\nNetwork Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
