import requests

apikey = 'b24246ea4943669ee31732346370d8bb'

address = f"http://api.openweathermap.org/data/2.5/weather"

user_location = input(f'\nKerro paikkakunta: ')

def get_weather(user_location):
    parameters = {"q": user_location, "appid": apikey, "units": "metric", "lang": "fi"}


    try:
        answer = requests.get(address, params = parameters)
        data = answer.json()

        if answer.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f'\nSää on  {user_location} on {description}, {temp} astetta celcius')

        else:
            print(f"Tapahtui virhe. :(")

    except requests.exceptions.RequestException as e:
        print(f"Tapahtui verkkovirhe {e} :(")

get_weather(user_location)
