from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "d46cf340288b2b705f6b5883a4e0e08e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DEMO_DATA = {
    "mumbai":     {"city": "Mumbai",     "country": "IN", "temperature": 32, "feels_like": 38, "humidity": 78, "wind_speed": 14.4, "description": "Partly Cloudy",    "icon_url": "https://openweathermap.org/img/wn/02d@2x.png", "visibility": 6.0, "pressure": 1008},
    "delhi":      {"city": "Delhi",      "country": "IN", "temperature": 41, "feels_like": 44, "humidity": 25, "wind_speed": 18.0, "description": "Clear Sky",         "icon_url": "https://openweathermap.org/img/wn/01d@2x.png", "visibility": 8.0, "pressure": 998},
    "aurangabad": {"city": "Aurangabad", "country": "IN", "temperature": 36, "feels_like": 39, "humidity": 40, "wind_speed": 12.6, "description": "Sunny",             "icon_url": "https://openweathermap.org/img/wn/01d@2x.png", "visibility": 9.0, "pressure": 1002},
    "london":     {"city": "London",     "country": "GB", "temperature": 17, "feels_like": 15, "humidity": 65, "wind_speed": 21.6, "description": "Light Rain",        "icon_url": "https://openweathermap.org/img/wn/10d@2x.png", "visibility": 7.0, "pressure": 1015},
    "new york":   {"city": "New York",   "country": "US", "temperature": 24, "feels_like": 23, "humidity": 55, "wind_speed": 16.2, "description": "Scattered Clouds",  "icon_url": "https://openweathermap.org/img/wn/03d@2x.png", "visibility": 10.0,"pressure": 1020},
    "tokyo":      {"city": "Tokyo",      "country": "JP", "temperature": 28, "feels_like": 30, "humidity": 70, "wind_speed": 10.8, "description": "Overcast Clouds",   "icon_url": "https://openweathermap.org/img/wn/04d@2x.png", "visibility": 8.0, "pressure": 1010},
    "paris":      {"city": "Paris",      "country": "FR", "temperature": 20, "feels_like": 19, "humidity": 60, "wind_speed": 14.4, "description": "Clear Sky",         "icon_url": "https://openweathermap.org/img/wn/01d@2x.png", "visibility": 9.5, "pressure": 1018},
    "pune":       {"city": "Pune",       "country": "IN", "temperature": 30, "feels_like": 33, "humidity": 55, "wind_speed": 9.0,  "description": "Few Clouds",        "icon_url": "https://openweathermap.org/img/wn/02d@2x.png", "visibility": 8.5, "pressure": 1005},
}

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "humidity": data["main"]["humidity"],
                "wind_speed": round(data["wind"]["speed"] * 3.6, 1),
                "description": data["weather"][0]["description"].title(),
                "icon_url": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                "visibility": round(data.get("visibility", 0) / 1000, 1),
                "pressure": data["main"]["pressure"],
                "demo": False
            }
            return weather, None

        elif response.status_code == 401:
            # API key not active yet — try demo data
            key = city.lower().strip()
            if key in DEMO_DATA:
                demo = dict(DEMO_DATA[key])
                demo["demo"] = True
                return demo, None
            return None, f"'{city}' is not in demo mode. Try: Mumbai, Delhi, Aurangabad, London, New York, Tokyo, Paris, Pune"

        elif response.status_code == 404:
            return None, "City not found. Please check the city name and try again."
        else:
            return None, "Error fetching weather data. Please try again later."

    except requests.exceptions.Timeout:
        return None, "Request timed out. Please check your connection and try again."
    except requests.exceptions.ConnectionError:
        return None, "Connection error. Please check your internet connection."
    except Exception:
        return None, "An unexpected error occurred. Please try again."


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Please enter a city name."
        elif len(city) < 2:
            error = "City name must be at least 2 characters."
        elif any(char.isdigit() for char in city):
            error = "City name should not contain numbers."
        else:
            weather, error = get_weather(city)

    return render_template("index.html", weather=weather, error=error, city=city)


if __name__ == "__main__":
    app.run(debug=True)