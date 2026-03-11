# Weather Forecast CLI Tool

A Python CLI application that fetches and displays real-time weather data using the [OpenWeatherMap REST API](https://openweathermap.org/api).

## Features
- Real-time weather data via REST API with API key authentication
- Structured JSON parsing for temperature, humidity, wind speed, and more
- Robust error handling for invalid city names, bad API keys, and network failures

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Loki-3103/weather-forecast-cli.git
   cd weather-forecast-cli
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**  
   Get a free API key from [openweathermap.org](https://openweathermap.org/api) and replace `your_api_key_here` in `weather.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

## Usage

```bash
# Interactive mode
python weather.py

# Pass city as argument
python weather.py London
python weather.py "New York"
```

## Example Output

```
=============================================
  Weather Report: Chennai, IN
=============================================
  Condition     : Haze
  Temperature   : 33.4°C (Feels like 38.1°C)
  Humidity      : 72%
  Pressure      : 1007 hPa
  Wind Speed    : 4.1 m/s
  Visibility    : 3500 m
=============================================
```

## Tech Stack
- Python 3.x
- `requests` library
- OpenWeatherMap REST API

## Error Handling
- Invalid city name → clear error message, non-zero exit
- Invalid API key → prompt to check credentials
- Network failure / timeout → connection error message

## Author
**Logesh T** – [GitHub](https://github.com/Loki-3103) | [LinkedIn](https://linkedin.com/in/logesh-t-/)
