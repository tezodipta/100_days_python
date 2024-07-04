import requests

Endpoint = "https://opentdb.com/api.php"
parameter = {
    "amount":10,
    "type":"boolean",
}

response = requests.get(url=Endpoint,params=parameter)
response.raise_for_status()

data = response.json()
question_data = data["results"]