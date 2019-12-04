import json

import pandas as pd
import requests


class eventObj:

	def __init__(self,
	             title="",
	             ScienceEvent=False,
	             VisualArtsEvent=False,
	             MusicEvent=False,
	             ScreeningEvent=False,
	             TheatreEvent=False,
	             TalkEvent=False,
	             GeneralEvent=False,
	             date="",
	             time="",
	             locationName="",
	             locationURL="",
	             suitableFor="",
	             source="",
	             description="",
	             other="",
	             contact="",
	             cost="",
	             link=""):
		self.source = source.replace("\n", " ,")
		self.ScienceEvent = ScienceEvent
		self.VisualArtsEvent = VisualArtsEvent
		self.MusicEvent = MusicEvent
		self.ScreeningEvent = ScreeningEvent
		self.TheatreEvent = TheatreEvent
		self.TalkEvent = TalkEvent
		self.GeneralEvent = GeneralEvent
		self.suitableFor = suitableFor.replace("\n", " ,")
		self.title = title.replace("\n", " ,")
		self.date = date.replace("\n", " ,")
		self.time = time.replace("\n", " ,")
		self.locationName = locationName.replace("\n", " ,")
		self.locationURL = locationURL.replace("\n", " ,")
		self.description = description.replace("\n", " ,")
		self.contact = contact.replace("\n", " ,")
		self.cost = cost.replace("\n", " ,")
		self.other = other.replace("\n", " ,")
		self.link = link.replace("\n", " ,")


def get_category(cat, sub_cat):
	science = 'ScienceEvent'
	visual = 'VisualArtsEvent'
	music = 'MusicEvent'
	screen = 'ScreeningEvent'
	theatre = 'TheatreEvent'
	talk = 'TalkEvent'
	general = 'Event'
	cat_dict = {
	    science: ['enogastronomia', 'eventi rifugi'],
	    visual: ['mercati e mercatini', 'mostre', 'spettacoli pirotecnici', 'visite guidate'],
	    music: ['feste e sagre', 'festival', 'fiere', 'musica'],
	    screen: ['cinema'],
	    theatre: ['teatro/danza', 'intrattenimento della località', 'folklore'],
	    talk: ['conferenze/congressi', 'rifugi aperti'],
	    general: ['altro', 'eventi culturali', 'sport', 'top eventi sport']
	}


def rm_main(JSONString):
	events = []
	trentoTodayE = json.loads(JSONString)
	for event in trentoTodayE:
		if 'Title' not in event:
			continue
		if 'category' not in event:
			event['category'] = ""
		if 'location' not in event:
			event['location'] = ""
		if 'location_url' not in event:
			event['location_url'] = ""
		events.append(
		    eventObj(
		        source="trentoTodayE",
		        category="Cultural",
		        subCategory=event['category'],
		        title=event['Title'],
		        cost=event['price'],
		        locationName=event['location'],
		        locationURL=event['location_url'],
		        description=event['description'],
		        date=event['date'],
		        time=event['time'],
		        link=event['Link']
		        # many tags!
		    ))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
