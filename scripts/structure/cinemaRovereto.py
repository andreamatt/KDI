import json

import pandas as pd
import requests


class eventObj:
	def __init__(self, title="", category="", subCategory="", date="", time="", locationName="", locationURL="",
				 suitableFor="", source="", description="", other="", contact="", cost="", link="", subSubCategory=""):
		self.source = source.replace("\n", " ,")
		self.category = category.replace("\n", " ,")
		self.subCategory = subCategory.replace("\n", " ,")
		self.subSubCategory = subSubCategory.replace("\n", " ,")
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


def rm_main(JSONString):
	events = []
	cinemaRovereto = json.loads(JSONString)
	for movie in cinemaRovereto['movies']:
		for dateAndTime in movie['time']:
			events.append(eventObj(
					source="cinemaRovereto",
					title=movie['title'],
					description=movie['description'],
					subCategory=movie['genre'],
					category="Movie",
					date=dateAndTime['day'],
					time=dateAndTime['hour'],
					contact=cinemaRovereto['Contact'],
					cost=cinemaRovereto['Price'],
					locationName=cinemaRovereto['Location'],
					locationURL=cinemaRovereto['URL'],
					link=movie['Link']
					# length :-??
			))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
