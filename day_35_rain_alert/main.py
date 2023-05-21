import requests
import os
from twilio.rest import Client
#using openweather api
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = ""
account_sid = ''
auth_token = ''


weather_params = {
    #pittsburgh
    "lat": 40.44,
    "lon": -79.99,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    #using twilio api
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='',
        to=''
    )
    print(message.status)
else:
    print("It will not rain today!")
