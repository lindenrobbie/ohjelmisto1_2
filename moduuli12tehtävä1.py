import requests

osoite = f"https://api.chucknorris.io/jokes/random"

response = requests.get(osoite)
data = response.json()
vitsi = data["value"]

print(f"\n{vitsi}")