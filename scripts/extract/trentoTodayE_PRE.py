import json
import requests


def rm_main():
	url = 'http://194.32.77.99/KDI/dataset/trentoTodayE.json'
	obj = json.loads(requests.get(url).text)
	
	for event in obj['events']:
		# if no category, get first tag
		if 'category' not in event:
			if 'tags' in event:
				event['category'] = event['tags'][0]['name']
				
	return json.dumps(obj)
