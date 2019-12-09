import json
import requests
from pandas import DataFrame as DF

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(*JSONStrings):
	results = {general: [], science: [], visual: [], music: [], screen: [], theatre: [], talk: [], creative_movies: []}
	for jsonstring in JSONStrings:
		source_events = json.loads(jsonstring)
		for entity_type, event_list in source_events.items():
			results[entity_type].extend(event_list)

	return json.dumps(results)