import requests

addy = f"https://api.chucknorris.io/jokes/random"

response = requests.get(addy)
data = response.json()
joke = data["value"]

print(f"\n{joke}")