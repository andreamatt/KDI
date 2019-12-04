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
		gen = GeneralEvent(movie['title'], movie['Price'], movie['description'], movie['cinemaURL'], movie['length'], movie['language'], True,
		                   movie['location'])
		screen = ScreeningEvent('', movie['originalName'], movie['genre'], movie['length'])
		work = CreativeWork(movie['title'], movie['director'], movie['createDate'], movie['URL'])

		for dateAndTime in movie['time']:
			date = Time(date['day'], date['day'], date['startTime'], '')
			event = {**gen, **screen, **work, **date}
			events.append(event)

	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
