import json
import requests

sarja=input("Anna sarja minkä tiedot haluat: ")

pyynto= "https://api.tvmaze.com/search/shows?q=" + sarja
vastaus=requests.get(pyynto).json()
print(json.dumps(vastaus, indent=2))