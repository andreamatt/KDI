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
		if l != "" and l != None and isinstance(l, str):
			result += f'/{quote(l)}'
		else:
			result += f'/{quote("_")}'
	return result


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/DBG/structure.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	events = []
	movies = []
	cineworldTrento = json.loads(JSONString)
	for movie in cineworldTrento['movies']:
		movie['director'] = movie['director'][0] if len(movie['director']) > 0 else ''
		movie['genre'] = movie['genre'][0] if len(movie['genre']) > 0 else ''

		scr = ScreeningEvent('')
		m = Movie(movie['originalName'], movie['genre'], movie['length'])
		work_URI = text_to_URI([movie['wikiUrl']])
		work = CreativeWork(movie['title'], movie['director'], movie['year'], movie['wikiUrl'], work_URI)

		for schedule in movie['schedule']:
			gen = GeneralEvent(movie['title'], schedule['Price'], movie['description'], movie['Link'], movie['length'], movie['language'], True,
			                   schedule['location'])
			gen['work_URI'] = work_URI

			for t in schedule['time']:
				hours = t['hour'].split('-')
				date = Time(schedule['day'], schedule['day'], hours[0], hours[1])
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
