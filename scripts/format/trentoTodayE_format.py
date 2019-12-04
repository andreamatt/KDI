import json
import re
import requests


def rm_main(JSONString):
	#url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/trentoTodayE.json'
	#obj = json.loads(requests.get(url).text)
	obj = json.loads(JSONString)

	known_times = {'tutto il giorno': '00:00-23:59'}

	events = []
	for event in obj:
		if 'date' in event:
			dates = re.findall(r'\d\d/\d\d/\d\d\d\d', event['date'])
			if len(set(dates)) == 1:
				event['startDate'] = event['endDate'] = dates[0]
			elif len(set(dates)) == 2:
				event['startDate'] = dates[0]
				event['endDate'] = dates[1]
		else:
			event['date'] = ""

		new_time = ""
		if 'time' in event:
			if event['time'] in known_times:
				new_time = known_times[event['time']]
			else:
				r = r'(?:(?:\d\d|\d)[:.]\d\d)|(?:\d\d|\d)'
				times = re.findall(r, event['time'])
				if len(times) == 1:
					new_time = times[0]
				elif len(times) == 2:
					new_time = f'{times[0]}-{times[1]}'
		event['time'] = new_time

		events.append(event)
	return json.dumps(events)
