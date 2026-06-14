# WeatherNow – Real-Time Weather App
Built by **Khan Mansafa** | Python Flask + OpenWeatherMap API

## Features
- Real-time weather data for any city worldwide
- Displays temperature, humidity, wind speed, visibility, and pressure
- Dynamic weather icons from OpenWeatherMap
- Mobile-friendly responsive design with Bootstrap 5
- Robust error handling for invalid city names, network issues, etc.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons, JavaScript
- **API:** OpenWeatherMap (Current Weather Data)

---

## Setup Instructions

### 1. Get a Free API Key
1. Go to https://openweathermap.org/api
2. Sign up for a free account
3. Go to **API keys** tab and copy your key

### 2. Add Your API Key
Open `app.py` and replace:
```python
API_KEY = "your_api_key_here"
```
with your actual API key:
```python
API_KEY = "abc123youractualkey"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
Go to: **http://127.0.0.1:5000**

---

## Project Structure
```
weather_app/
├── app.py                  # Flask backend & API logic
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Main HTML page (Jinja2 template)
└── static/
    ├── css/
    │   └── style.css       # Custom styles
    └── js/
        └── script.js       # Frontend JS
```

---

## Error Handling
- Empty input → validation message
- Invalid city name → user-friendly error
- API timeout → connection error message
- Invalid API key → clear warning message
