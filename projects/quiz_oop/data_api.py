import requests

parameters = {
    "amount" : 10,
    "type" : "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
question_api = data["results"]