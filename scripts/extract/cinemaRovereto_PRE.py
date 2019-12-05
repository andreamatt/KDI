import json

import requests


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/cinemaRovereto.json'
	obj = json.loads(requests.get(url).text)
	info = {
	    'location': "Piazza Rosmini 18/A. Rovereto (TN)",
	    'contact': "0464 421216",
	    'price': "8,50 €",
	    'cinemaURL': "http://www.supercinemarovereto.it/"
	}

	for movie in obj['movies']:
		movie['description'] = movie['description'].replace('\n', '; ')
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

		movie.update(info)
	return json.dumps(obj)
