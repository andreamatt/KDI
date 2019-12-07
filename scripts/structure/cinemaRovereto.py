import json
import pandas as pd
import requests

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONString):

	events = []
	cinemaRovereto = json.loads(JSONString)
	for movie in cinemaRovereto['movies']:
		movie['director'] = movie['director'][0] if len(movie['director']) > 0 else ''
		movie['genre'] = movie['genre'][0] if len(movie['genre']) > 0 else ''

		gen = GeneralEvent(movie['title'], movie['price'], movie['description'], movie['cinemaURL'], movie['length'], movie['language'], True,
		                   movie['location'])
		scr = ScreeningEvent('')
		m = Movie(movie['originalName'], movie['genre'], movie['length'])
		work = CreativeWork(movie['title'], movie['director'], movie['year'], movie['wikiUrl'])

		for dateAndTime in movie['time']:
			for hour in dateAndTime['hour'].split('-'):
				date = Time(dateAndTime['day'], dateAndTime['day'], hour, '')
				event = {}
				for k, v in gen.items():
					event[f'GEN_{k}'] = v
				for k, v in scr.items():
					event[f'SCREEN_{k}'] = v
				for k, v in m.items():
					event[f'MOVIE_{k}'] = v
				for k, v in work.items():
					event[f'WORK_{k}'] = v
				for k, v in date.items():
					event[f'TIME_{k}'] = v
				events.append(event)

	return json.dumps({screen: events})
