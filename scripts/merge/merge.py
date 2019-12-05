import json
import requests
from pandas import DataFrame as DF

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(*JSONStrings):
	events = {general: [], science: [], visual: [], music: [], screen: [], theatre: [], talk: []}
	for jsonstring in JSONStrings:
		source_events = json.loads(jsonstring)
		for category, event_list in source_events.items():
			events[category].extend(event_list)

	return json.dumps(events)