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


def rm_main():
	events = []
	url = 'http://194.32.77.99/KDI/dataset/cineTrento.json'
	cineTrento = json.loads(requests.get(url).text)
	for movie in cineTrento['movies']:
		for schedule in movie['schedule']:
			for time in schedule['time']:
				events.append(eventObj(
						source="cineTrento",
						title=movie['title'],
						description=movie['description'],
						subCategory=movie['genre'],
						category="Movie",
						date=schedule['day'],
						locationName=schedule['location'],
						time=time['hour'] + "--LEN--" + movie['lenght']
				))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
