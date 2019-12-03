from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import requests
import json

API_key = "AIzaSyB211Jj9rzG_io-a_DBNx_aaALMdOaNiug"
MAX_WORKERS = 100

locations = [
    "centro storico, piazza Cesare Battisti, Tesero",
    "Quartiere Le Albere,&&&\"@\%#\% Via Roberto da Sanseverino" # TEST FOR SPECIAL CHARS
]

geocoded = {}
errors = {}

def geocode(name):
    if name in geocoded:
        return geocoded[name]
    
    url = f'https://maps.googleapis.com/maps/api/geocode'\
    f'/json?key={API_key}&region=it&address={name}'
    
    response = requests.get(url)

    if response.ok:
        results = response.json()
        geocoded[name] = results
        return results
    else:
        errors[name] = response.text
        return None



def geocodeALL():
    with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _ in executor.map(geocode, locations):
            pass


geocodeALL()

with open('geocoded.json', 'w') as outfile:
    json.dump(geocoded, outfile, indent="\t")

with open('geocoded_errors.json', 'w') as outfile:
    json.dump(errors, outfile, indent="\t")


