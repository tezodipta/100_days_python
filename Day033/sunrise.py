import requests
from datetime import datetime
time_now = datetime.now()
import geocoder  
g = geocoder.ip('me')
my_lat = g.latlng[0]
my_lng = g.latlng[1]



parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0] 
print(sunrise,sunset)