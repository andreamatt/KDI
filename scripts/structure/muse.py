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


def rm_main(jsonString):
	events = []
	muse = json.loads(jsonString)
	for event in muse['events']:
		if "name" not in event:
			continue
		events.append(
		    eventObj(
		        source="muse",
		        category="Cultural",
		        subCategory=event['Subcategory'],
		        title=event['name'],
		        suitableFor=event["target"],
		        date=event['when'],
		        time=event['time'],
		        locationName=event['where'],
		        description=event['description'],
		        cost=event['cost'],
		        link=event['link'],
		        contact=muse['contact']))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
