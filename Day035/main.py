import requests
import geocoder 
from twilio.rest import Client

# twilio info
account_sid = 'id'
auth_token = 'auth token'

# open weather info
endpoint = "url"
API_KEY = "api key"

# current location
g = geocoder.ip('me')
my_lat = g.latlng[0]
my_lng = g.latlng[1]


parameter = {
    "lat":my_lat,
    "lon":my_lng,
    "appid":API_KEY,
    "exclude": "current,minutely,daily"

}

# fetching api
response = requests.get(url=endpoint,params=parameter)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True

if will_rain:
    result = "Bring an Umbrella"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=result,
        from_='+15735152782',
        to='number'
    )
    print(message.sid)


