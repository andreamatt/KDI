import json
import requests

fields = ['Title', 'Link', 'category', 'location', 'price', 'date', 'time', 'description']


def fill_event(e):
	for f in fields:
		e[f] = e.get(f, '')


constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)

cat_dict = {
    science: ['enogastronomia', 'eventi rifugi'],
    visual: ['mercati e mercatini', 'mostre', 'spettacoli pirotecnici', 'visite guidate'],
    music: ['feste e sagre', 'festival', 'fiere', 'musica'],
    screen: ['cinema'],
    theatre: ['teatro/danza', 'intrattenimento della località', 'folklore'],
    talk: ['conferenze/congressi', 'rifugi aperti'],
    general: ['altro', 'eventi culturali', 'sport', 'top eventi sport']
}


def get_category(cat):
	for k, v in cat_dict.items():
		if k != general and cat in v:
			return k
	return general


def rm_main():
	url = 'https://raw.githubusercontent.com/andreamatt/KDI/master/dataset/trentoTodayE.json'
	obj = json.loads(requests.get(url).text)
	events = [e for e in obj['events'] if 'Title' in e]
	for event in events:
		# if no category, get first tag
		if 'category' not in event:
			if 'tags' in event:
				event['category'] = event['tags'][0]['name']
		event['category'] = get_category(event)
		fill_event(event)

	return json.dumps(events)
