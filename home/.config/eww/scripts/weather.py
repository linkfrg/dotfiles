import requests, json

icons = {
    "01d": "",
    "01n": "",
    "02d": "",
    "02n": "",
    "03d": "󰖐",
    "03n": "󰖐",
    "04d": "",
    "04n": "",
    "09d": "",
    "09n": "",
    "10d": "",
    "10n": "",
    "11d": "",
    "11n": "",
    "13d": "",
    "13n": "",
    "50d": "󰖑",
    "50n": "󰖑" 
}


API_TOKEN = "69c655f5c49d7a1612da1c5a0617d786"
UNITS = 'metric'
LANG = 'ru'
LOCATION = requests.get("https://location.services.mozilla.com/v1/geolocate?key=geoclue").json()['location']

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LOCATION['lat']}&lon={LOCATION['lng']}&appid={API_TOKEN}&lang={LANG}&units={UNITS}").json()


print(str(json.dumps({
    "icon": icons[response['weather'][0]['icon']],
    "temp": str(round(response['main']['temp'])) + "°",
    "desc": response['weather'][0]['description'].capitalize()
})))
