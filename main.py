import requests
import os
from twilio.rest import Client

MY_LAT = 14.412993
MY_LONG = 120.973679
MY_COUNT = 4

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":api_key,
    "cnt":MY_COUNT
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
list_data = data["list"]

will_rain = False

for status in list_data:
    weather_id = status["weather"][0]["id"]
    weather_desc = status["weather"][0]["description"]
    print(weather_desc)
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("It will rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_="whatsapp:+14155238886",
        to="whatsapp:+639457643338",
    )
    print(message.status)
