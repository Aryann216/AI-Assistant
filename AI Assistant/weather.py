#https://www.google.com/search?q=weather+patna&ie=UTF-8
#user agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36
#     span    id="wob_tm"



import requests

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Foggy", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    95: "Thunderstorm",
}

def get_weather(latitude=25.5941, longitude=85.1376, city="Patna"):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
        "timezone": "Asia/Kolkata",
    }
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        c = r.json()["current"]
        desc = WEATHER_CODES.get(c["weather_code"], "Unknown weather")
        return (f"Weather in {city}: {desc}, temperature {c['temperature_2m']} degrees, "
                f"feels like {c['apparent_temperature']}, humidity {c['relative_humidity_2m']} percent, "
                f"wind {c['wind_speed_10m']} kilometres per hour.")
    except requests.exceptions.RequestException as e:
        return f"Weather request failed: {e}"
    except (KeyError, ValueError) as e:
        return f"Unable to read weather data: {e}"

if __name__ == "__main__":
    print(get_weather())
