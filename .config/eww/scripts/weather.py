#!/usr/bin/python

import requests, json, sys, time, os
from datetime import datetime

API_TOKEN = "8236f5b850a3467c915160518231909"
CITY = "Astana"
EXCLUDE = "hourly"
AQI = "no"
DAYS = 2

URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_TOKEN}&q={CITY}&aqi={AQI}&days={DAYS}"

def get_icon(code):
    icons = {
        "1000_1": "", "1000_0": "",
        "1003_1": "", "1003_0": "",
        "1006_1": "󰖐", "1006_0": "󰖐",
        "1009_1": "", "1009_0": "",
        "1030_1": "", "1030_0": "",
        "1063_1": "", "1063_0": "",
        "1066_1": "", "1066_0": "",
        "1069_1": "", "1069_0": "",
        "1072_1": "󰙿", "1072_0": "󰙿",
        "1087_1": "", "1087_0": "",
        "1114_1": "", "1114_0": "",
        "1117_1": "", "1117_0": "",
        "1135_1": "󰖑", "1135_0": "󰖑",
        "1147_1": "󰖑", "1147_0": "󰖑",
        "1150_1": "󰙿", "1150_0": "󰙿",
        "1153_1": "󰙿", "1153_0": "󰙿",
        "1168_1": "󰙿", "1168_0": "󰙿",
        "1171_1": "󰙿", "1171_0": "󰙿",
        "1180_1": "", "1180_0": "",
        "1183_1": "", "1183_0": "",
        "1186_1": "", "1186_0": "",
        "1189_1": "", "1189_0": "",
        "1192_1": "", "1192_0": "",
        "1195_1": "", "1195_0": "",
        "1198_1": "󰙿", "1198_0": "󰙿",
        "1201_1": "󰙿", "1201_0": "󰙿",
        "1204_1": "󰙿", "1204_0": "󰙿",
        "1207_1": "󰙿", "1207_0": "󰙿",
        "1210_1": "󰖘", "1210_0": "󰖘",
        "1213_1": "󰖘", "1213_0": "󰖘",
        "1216_1": "󰖘", "1216_0": "󰖘",
        "1219_1": "󰖘", "1219_0": "󰖘",
        "1222_1": "󰼶", "1222_0": "󰼶",
        "1225_1": "󰼶", "1225_0": "󰼶",
        "1237_1": "󰖒", "1237_0": "󰖒",
        "1240_1": "", "1240_0": "",
        "1243_1": "", "1243_0": "",
        "1246_1": "", "1246_0": "",
        "1249_1": "󰙿", "1249_0": "󰙿",
        "1252_1": "󰙿", "1252_0": "󰙿",
        "1255_1": "󰖘", "1255_0": "󰖘",
        "1258_1": "󰖘", "1258_0": "󰖘",
        "1261_1": "󰙿", "1261_0": "󰙿",
        "1264_1": "󰙿", "1264_0": "󰙿",
        "1273_1": "", "1273_0": "",
        "1276_1": "", "1276_0": "",
        "1279_1": "", "1279_0": "",
        "1282_1": "", "1282_0": "",
    }

    return icons[code]

def main():
    while True:
        try:
            response = requests.get(URL).json()
            break
        except requests.exceptions.ConnectionError:
            print("Failed to get response from url! Retrying...")
            time.sleep(2)
    hourly = []
    for day in response['forecast']['forecastday']:
        for hour in day['hour']:
            data = {"time": hour['time'][-5:],
                    "temp": f"{round(hour['temp_c'])}°",
                    "icon": get_icon(f"{hour['condition']['code']}_{hour['is_day']}")
                    }
            hourly.append(data)

    for hour in hourly:
        if hour['time'] == f"{datetime.now().strftime('%H')}:00":
            hourly = hourly[hourly.index(hour):]
            break
    hourly = hourly[:4]
    data = {
        "location": response["location"]["name"],
        "maxtemp": f"{round(response['forecast']['forecastday'][0]['day']['maxtemp_c'])}°",
        "mintemp": f"{round(response['forecast']['forecastday'][0]['day']['mintemp_c'])}°",
        "current": {
            "temp": f"{round(response['current']['temp_c'])}°",
            "text": response['current']['condition']['text'],
            "icon": get_icon(f"{response['current']['condition']['code']}_{response['current']['is_day']}"),
        },
        "hourly": hourly
    }

    return data

if __name__ == "__main__":
    while True:
        try:
            sys.stdout.write(json.dumps(main()) + "\n")
            sys.stdout.flush()
            os.system(f"eww update weather='{json.dumps(main())}'")
            time.sleep(1800)
        except KeyboardInterrupt:
            exit(0)
