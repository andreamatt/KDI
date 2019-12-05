import json
import requests

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/structure.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	trentoTodayE = json.loads(JSONString)
	events = {}

	for e in trentoTodayE:
		gen = GeneralEvent(e['name'], e['cost'], e['description'], e['link'], '', '', '', e['where'])

		period = '' if len(e['days']) == 0 else Period(e['days'], '', '', '', 'daily')
		for time in e['time']:
			for date in e['when']:
				if '-' in date:
					if '-' in time:
						time = Time(date.split('-')[0], date.split('-')[1], time.split('-')[0], time.split('-')[1])

				pass
			else:
				pass

		event = {}
		for k, v in gen.items():
			event[f'GEN_{k}'] = v
		for k, v in time.items():
			event[f'TIME_{k}'] = v

		if e['Subcategory'] not in events:
			events[e['Subcategory']] = []
		events[e['Subcategory']].append(event)

	#events = [ob.__dict__ for ob in events]
	#df = pd.DataFrame(events)
	#return df

	return json.dumps(events)