from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import requests
import json

API_KEY = "AIzaSyB211Jj9rzG_io-a_DBNx_aaALMdOaNiug"
MAX_WORKERS = 100
FIELDS = [
    "name",
    "geometry",
    "opening_hours",
    "formatted_address",
    "permanently_closed",
    "type",
    "vicinity",
    "formatted_phone_number",
    "international_phone_number",
    "opening_hours",
    "website",
    "price_level",
    "rating",
    "user_ratings_total"
]

DETAILS_FIELDS = ','.join(FIELDS)

locations = [
    "oasi del gusto, volano",
    # TEST FOR SPECIAL CHARS:
    "MUSE, Quartiere Le Albere,&&&\"@\%#\% Via Roberto da Sanseverino"
]

search_results = {}
details_results = {}
errors = {}


def place_search(name):
    if name in search_results:
        return search_results[name]

    url = f'https://maps.googleapis.com/maps/api/place'\
    f'/findplacefromtext/json?key={API_KEY}&region=it&inputtype=textquery&input={name}'

    response = requests.get(url)

    if response.ok:
        results = response.json()
        search_results[name] = results
        return results
    else:
        errors[name] = response.text
        return None


def place_details(name):
    if name in details_results:
        return details_results[name]

    if len(search_results[name]['candidates']) == 0:
        details_results[name] = "No results"
        return "No results"

    candidate = search_results[name]['candidates'][0]
    place_id = candidate['place_id']
    url = f'https://maps.googleapis.com/maps/api/place'\
    f'/details/json?key={API_KEY}&region=it&place_id={place_id}&fields={DETAILS_FIELDS}'
    response = requests.get(url)

    if response.ok:
        result = response.json()
        details_results[name] = result
        return result
    else:
        errors[name] = response.text
        return None


def place_search_ALL():
    with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _ in executor.map(place_search, locations):
            pass


def place_details_ALL():
    with PoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _ in executor.map(place_details, search_results.keys()):
            pass


place_search_ALL()
place_details_ALL()

with open('places.json', 'w') as outfile:
    json.dump(details_results, outfile, indent="\t")

with open('places_errors.json', 'w') as outfile:
    json.dump(errors, outfile, indent="\t")
