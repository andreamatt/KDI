import json

import pandas as pd
import requests

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/DBG/structure.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	events = {}
	mart = json.loads(JSONString)
	for e in mart:
		gen = GeneralEvent(e['name'], e['cost'], e['comment'], e['link'], '', '', '', e['location'])

		startDate = e['date']
		endDate = e['date']
		time = e['time'].split('-')
		startTime = time[0]
		endTime = time[0]
		if len(time) > 1:
			endTime = time[1]
		time = Time(startDate, endDate, startTime, endTime)

		event = {}
		for k, v in gen.items():
			event[f'GEN_{k}'] = v
		for k, v in time.items():
			event[f'TIME_{k}'] = v

		if e['category'] not in events:
			events[e['category']] = []

		events[e['category']].append(event)

	return json.dumps(events)
