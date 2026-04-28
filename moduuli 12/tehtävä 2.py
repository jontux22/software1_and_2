import requests

api_key = "YOUR_API_KEY"

try:
    city = input("Enter municipality name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print(f"Virhe: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Yhteysvirhe: {e}")