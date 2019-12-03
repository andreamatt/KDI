import json
import requests


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/visitTrentino.json'
	obj = json.loads(requests.get(url).text)

	for event in obj['events']:
		# if no category, get first tag
		event['category'] = event['category'][len('Tipologia\n'):]
		event['location'] = event['location'][len('Località\n'):]
		event['date'] = event['date'][len('Periodo\n'):]

	return json.dumps(obj)
