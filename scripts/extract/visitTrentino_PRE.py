import json
import requests


def rm_main():
	url = 'http://194.32.77.99/KDI/dataset/visitTrentino.json'
	obj = json.loads(requests.get(url).text)
	return json.dumps(obj)
