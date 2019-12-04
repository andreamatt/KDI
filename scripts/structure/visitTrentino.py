import json
import pandas as pd
import requests

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONString):
	visitTrentino = json.loads(JSONString)
	events = {}

	for e in visitTrentino:
		gen = GeneralEvent(e['Title'], e['Prices'], e['description'], e['link'], '', '', '', e['location'])
		time = Time(e['startDate'], e['endDate'], e['startTime'], e['endTime'])
		event = {**gen, **time}

		if e['category'] not in events:
			events[e['category']] = []
		events[e['category']].append(event)

	#events = [ob.__dict__ for ob in events]
	#df = pd.DataFrame(events)
	#return df

	return json.dumps(events)
