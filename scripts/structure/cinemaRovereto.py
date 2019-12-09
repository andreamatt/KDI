import json
import pandas as pd
import requests
from urllib.parse import quote

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def text_to_URI(labels):
	result = BASE_URI
	for l in labels:
		if l != "" and l != None:
			result += f'/{quote(l)}'
		else:
			result += f'/{quote("_")}'
	return result


def rm_main(JSONString):

	events = []
	movies = []
	cinemaRovereto = json.loads(JSONString)
	for movie in cinemaRovereto['movies']:
		movie['director'] = movie['director'][0] if len(movie['director']) > 0 else ''
		movie['genre'] = movie['genre'][0] if len(movie['genre']) > 0 else ''

		gen = GeneralEvent(movie['title'], movie['price'], movie['description'], movie['cinemaURL'], movie['length'], movie['language'], True,
		                   movie['location'])
		scr = ScreeningEvent('')
		m = Movie(movie['originalName'], movie['genre'], movie['length'])
		work_URI = text_to_URI([movie['title'], movie['director'], movie['year'], movie['wikiUrl']])
		gen['work_URI'] = work_URI
		work = CreativeWork(movie['title'], movie['director'], movie['year'], movie['wikiUrl'], work_URI)

		for dateAndTime in movie['time']:
			for hour in dateAndTime['hour'].split('-'):
				date = Time(dateAndTime['day'], dateAndTime['day'], hour, '')
				event = {}
				for k, v in gen.items():
					event[f'GEN_{k}'] = v
				for k, v in scr.items():
					event[f'SCREEN_{k}'] = v
				for k, v in date.items():
					event[f'TIME_{k}'] = v
				events.append(event)

				creative_movie = {}
				for k, v in m.items():
					creative_movie[f'MOVIE_{k}'] = v
				for k, v in work.items():
					creative_movie[f'WORK_{k}'] = v
				movies.append(creative_movie)

	return json.dumps({screen: events, creative_movies: movies})
