import json

import pandas as pd
import requests
import re


def rm_main():
	url = 'http://194.32.77.99/KDI/dataset/mart.json'
	mart = json.loads(requests.get(url).text)
	for event in mart:
		if "locationName" not in event:
			event['locationName'] = ""
		
		email = re.search(r'[\w\.-]+@[\w\.-]+', event['comment'])
		event['contact'] = email.group(0)
		
		cost = re.search(r'Costo: € \d+', event['comment'])
		if cost is not None:
			event['cost'] = cost.group(0)
		else:
			event['cost'] = 'free'
		event['link'] = 'mart.trento.it/agenda.jsp'
		
	return json.dumps(mart)
