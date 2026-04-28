import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print(f"Virhe: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Yhteysvirhe: {e}")