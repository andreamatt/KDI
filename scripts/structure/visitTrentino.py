import json
import pandas as pd
import requests

utils_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/utils.py').text
exec(utils_txt)


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/DBG/structure.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	visitTrentino = json.loads(JSONString)
	events = {}

	for e in visitTrentino:
		gen = GeneralEvent(e['Title'], e['Prices'], e['description'], e['link'], '', '', '', e['location'])
		time = Time(e['startDate'], e['endDate'], e['startTime'], e['endTime'])
		event = {}
		for k, v in gen.items():
			event[f'GEN_{k}'] = v
		for k, v in time.items():
			event[f'TIME_{k}'] = v

		if e['category'] not in events:
			events[e['category']] = []
		events[e['category']].append(event)

	#events = [ob.__dict__ for ob in events]
	#df = pd.DataFrame(events)
	#return df

	return json.dumps(events)
