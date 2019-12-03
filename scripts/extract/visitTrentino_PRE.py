import json
import requests


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/visitTrentino.json'
	obj = json.loads(requests.get(url).text)

	for event in obj['events']:
		if 'category' in event:
			event['category'] = event['category'][len('Tipologia\n'):]
		else:
			event['category'] = ""
		
		if 'location' in event:
			event['location'] = event['location'][len('Località\n'):]
		else:
			event['location'] = ""

		if 'date' in event:
			event['date'] = event['date'][len('Periodo\n'):]
		else:
			event['date'] = ""

	return json.dumps(obj)
