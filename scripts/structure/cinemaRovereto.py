import json
import pandas as pd
import requests

# load classes
classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/temp.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	events = []
	cinemaRovereto = json.loads(JSONString)
	for movie in cinemaRovereto['movies']:
		gen = GeneralEvent(movie['title'], movie['price'], movie['description'], movie['cinemaURL'], movie['length'], movie['language'], True,
		                   movie['location'])
		screen = ScreeningEvent('')
		m = Movie(movie['originalName'], movie['genre'], movie['length'])
		work = CreativeWork(movie['title'], movie['director'], movie['year'], movie['wikiUrl'])

		for dateAndTime in movie['time']:
			for hour in dateAndTime['hour'].split('-'):
				date = Time(dateAndTime['day'], dateAndTime['day'], hour, '')
				event = {**gen, **screen, **m, **work, **date}
				events.append(event)

	return json.dumps({screen: events})
