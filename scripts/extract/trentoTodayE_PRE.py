import json
import requests


def rm_main():
	url = 'http://194.32.77.99/KDI/dataset/trentoTodayE.json'
	obj = json.loads(requests.get(url).text)
	return json.dumps(obj)
