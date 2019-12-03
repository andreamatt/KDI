import json

import requests


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/cinemaRovereto.json'
	obj = json.loads(requests.get(url).text)
	obj['Location'] = "Piazza Rosmini 18/A. Rovereto (TN)"
	obj['Contact'] = "0464 421216"
	obj['Price'] = "8,50 €"
	obj['URL'] = "http://www.supercinemarovereto.it/"
	for movie in obj['movies']:
		if 'time' not in movie:
			obj['movies'].remove(movie)
			continue
		for dateAndTime in movie['time']:
			if movie['title'] == "CHIUSO":
				obj['movies'].remove(movie)
				break
			if isinstance(dateAndTime, str):
				obj['movies'].remove(movie)
				break
	return json.dumps(obj)
