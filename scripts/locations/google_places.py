from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import requests
import json
import pandas as pd


class Facility:

	def __init__(self, name="", telephone="", website="", mail="", hasParking="", animalsAllowed="", smokingAllowed="", isIndoor=""):
		self.name = name
		self.telephone = telephone
		self.website = website
		self.mail = mail
		self.hasParking = hasParking
		self.animalsAllowed = animalsAllowed
		self.smokingAllowed = smokingAllowed
		self.isIndoor = isIndoor


class GeoCoordinates:

	def __init__(self, latitude="", longitude="", altitude="", address="", addressLocality="", addressRegion="", postalCode=""):
		self.latitude = latitude
		self.longitude = longitude
		self.altitude = altitude
		self.address = address
		self.addressLocality = addressLocality
		self.addressRegion = addressRegion
		self.postalCode = postalCode


API_KEY = 'AIzaSyB211Jj9rzG_io-a_DBNx_aaALMdOaNiug'

MAX_WORKERS = 100

FIELDS = [
    "name", "geometry", "opening_hours", "formatted_address", "permanently_closed", "type", "vicinity", "formatted_phone_number",
    "international_phone_number", "opening_hours", "website", "price_level", "rating", "user_ratings_total"
]

DETAILS_FIELDS = ','.join(FIELDS)

geocoded = {}
search_results = {}
no_results = {}
details_results = {}
errors = {}


def place_search(name):
	if name in search_results:
		return search_results[name]

	url = f'https://maps.googleapis.com/maps/api/place'
	url += f'/findplacefromtext/json?key={API_KEY}&region=it&inputtype=textquery&input={name}'

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
	elif name in no_results:
		return no_results['name']

	if len(search_results[name]['candidates']) == 0:
		no_results[name] = geocode(name)
		return no_results[name]

	candidate = search_results[name]['candidates'][0]
	place_id = candidate['place_id']
	url = f'https://maps.googleapis.com/maps/api/place'
	url += f'/details/json?key={API_KEY}&region=it&place_id={place_id}&fields={DETAILS_FIELDS}'
	response = requests.get(url)

	if response.ok:
		result = response.json()['result']

		complete_position = geocode(result['formatted_address'])
		result['geocoded'] = complete_position

		details_results[name] = result
		return result
	else:
		errors[name] = response.text
		return None


def geocode(name):
	if name in geocoded:
		return geocoded[name]

	url = f'https://maps.googleapis.com/maps/api/geocode'
	url += f'/json?key={API_KEY}&region=it&address={name}'

	response = requests.get(url)

	if response.ok:
		results = response.json()['results']
		if len(results) > 0:
			geocoded[name] = results[0]
		else:
			geocoded[name] = ""
		return geocoded[name]
	else:
		errors[name] = response.text
		return None


def place_search_ALL(locations):
	with PoolExecutor(max_workers=MAX_WORKERS) as executor:
		for _ in executor.map(place_search, locations):
			pass


def place_details_ALL():
	with PoolExecutor(max_workers=MAX_WORKERS) as executor:
		for _ in executor.map(place_details, search_results.keys()):
			pass


def rm_main(locations):
	#locations = [loc for loc in list(events.loc[:, "locationName"]) if str(loc) != 'nan']

	facilities = []

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/locations.json', 'w') as outfile:
		#outfile.write(f'{loc},\n')
		json.dump(locations, outfile, indent='\t')

	place_search_ALL(locations)

	place_details_ALL()

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/places.json', 'w') as outfile:
		json.dump(details_results, outfile, indent="\t")

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/places_errors.json', 'w') as outfile:
		json.dump(errors, outfile, indent="\t")

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/no_results.json', 'w') as outfile:
		json.dump(no_results, outfile, indent="\t")

	for searched_name, result in details_results.items():
		fac = ""
		if 'point_of_interest' in result['types']:
			name = result['name']
			telephone = result.get('formatted_phone_number', '')
			website = result.get('website', '')
			mail = "No email from google to avoid spamming"
			# other fields are not available from google
			fac = Facility(name, telephone, website, mail)

		lat = result['geometry']['location']['lat']
		lng = result['geometry']['location']['lng']
		altitude = ""
		address = result['formatted_address']
		addressLocality = "WHAT IS IT??"
		addressRegion = "WHAT IS IT???"
		postalCode = ''
		for comp in result['geocoded']['address_components']:
			if 'postal_code' in comp['types']:
				postalCode = comp['long_name']
		coordinates = GeoCoordinates(lat, lng, altitude, address, addressLocality, addressRegion, postalCode)

		facilities.append({'locationText': searched_name, 'facility': "" if fac == "" else fac.__dict__, 'geocoordinates': coordinates.__dict__})

	# no results in google places, used google geocoding
	for searched_name, result in no_results.items():
		if result != "":
			geom = result['geometry']
			location = geom['location']
			lat = location['lat']
			lng = location['lng']
			altitude = ""
			address = result['formatted_address']
			addressLocality = "WHAT IS IT??"
			addressRegion = "WHAT IS IT???"
			#postalCode = [comp['long_name'] for comp in result['address_components'] if 'postal_code' in comp['types']][0]
			postalCode = ''
			for comp in result['address_components']:
				if 'postal_code' in comp['types']:
					postalCode = comp['long_name']
			coordinates = GeoCoordinates(lat, lng, altitude, address, addressLocality, addressRegion, postalCode)

			facilities.append({'locationText': searched_name, 'facility': "", 'geocoordinates': coordinates.__dict__})

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/script_res.json', 'w') as outfile:
		json.dump(facilities, outfile, indent='\t')

	facilities_DF = []
	for fac in facilities:
		obj = {'locationText': fac['locationText']}
		for k, v in fac['geocoordinates'].items():
			obj[f'GEO_{k}'] = v

		if fac['facility'] != '':
			for k, v in fac['facility'].items():
				obj[f'FAC_{k}'] = v

		facilities_DF.append(obj)

	return pd.DataFrame(facilities_DF)
