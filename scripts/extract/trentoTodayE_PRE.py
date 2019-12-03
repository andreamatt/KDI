import json
import requests


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/trentoTodayE.json'
	obj = json.loads(requests.get(url).text)
	
	for event in obj['events']:
		# if no category, get first tag
		if 'category' not in event:
			if 'tags' in event:
				event['category'] = event['tags'][0]['name']
				
	return json.dumps(obj)
