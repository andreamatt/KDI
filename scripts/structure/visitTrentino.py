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
	    science: ['escursioni', 'religione', 'auto e moto'],
	    visual: ['mostre', 'mercatini', 'fiere', 'inaugurazioni', 'turismo', 'moda'],
	    music: ['sagre', 'concerti', 'disco&feste'],
	    screen: ['cinema'],
	    theatre: ['teatri'],
	    talk: ['incontri', 'manifestazioni', 'talk'],
	    general: ['cibo e vino', 'sport', 'fitness', 'hobby', 'promozioni']
	}


def rm_main(JSONString):
	events = []
	visitTrentino = json.loads(JSONString)
	for event in visitTrentino:
		if 'Title' not in event:
			continue
		if 'fulldesc' not in event:
			event['fulldesc'] = ""
		if 'time' not in event:
			event['time'] = ""
		if 'category' not in event:
			event['category'] = ""
		if 'sub_title' not in event:
			event['sub_title'] = ""
		if 'contacts' not in event:
			event['contacts'] = ""
		if 'location' not in event:
			event['location'] = ""
		events.append(
		    eventObj(
		        source="visitTrentino",
		        category="Cultural",
		        subCategory=event['category'],
		        title=event['Title'],
		        date=event['date'],
		        time=event['time'],
		        link=event['link'],
		        locationName=event['location'],
		        description=event['fulldesc'],
		        other=event['sub_title'],
		        contact=json.dumps(event['contacts'])
		        # miniDesc,dates
		    ))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df