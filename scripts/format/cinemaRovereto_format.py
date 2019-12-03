import json
import re
import requests


def rm_main(JSONString):
	obj = json.loads(JSONString)
	movies = []
	for movie in obj['movies']:
		times = []
		for dateAndTime in movie['time']:
			hours = dateAndTime['hour']
			hours = hours.split('-')
			for hour in hours:
				hour = hour.replace(' ', '')
				hour = hour.replace('.', ':')
				day = dateAndTime['day']
				day = re.findall(r'\d+\/\d+\/\d+', day)
				day = day[0]
				day = day.replace('/', '-')
				times.append({
					"day" : day,
					"hour": hour
				})
		movie['time'] = times
		movies.append(movie)
	obj['movies'] = movies
	return json.dumps(obj)
