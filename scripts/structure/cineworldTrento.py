import json

import pandas as pd
import requests


class eventObj:
	def __init__(self, title="", category="", subCategory="", date="", time="", locationName="", locationURL="",
				 suitableFor="", source="", description="", other="", contact="", cost="", link="", subSubCategory=""):
		self.source = source
		self.category = category
		self.subCategory = subCategory
		self.subSubCategory = subSubCategory
		self.suitableFor = suitableFor
		self.title = title
		self.date = date
		self.time = time
		self.locationName = locationName
		self.locationURL = locationURL
		self.description = description
		self.contact = contact
		self.cost = cost
		self.other = other
		self.link = link


def rm_main(JSONString):
	cineworldTrento = json.loads(JSONString)
	events = []
	for movie in cineworldTrento['movies']:
		for schedule in movie['schedule']:
			for time in schedule['time']:
				events.append(eventObj(
						source="cineworldTrento",
						title=movie['title'],
						description=movie['description'],
						subCategory=movie['genre'],
						category="Movie",
						date=schedule['day'],
						locationName=schedule['location'],
						cost=schedule['Price'],
						contact=cineworldTrento['Contact'],
						link=cineworldTrento['Link'],
						time=time['hour'],
						other="--LEN--" + movie['lenght']
				))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
