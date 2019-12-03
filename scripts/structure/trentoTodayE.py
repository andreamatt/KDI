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
	events = json.loads(JSONString)
	for event in events:
		if 'Title' not in event:
			continue
		if 'category' not in event:
			event['category'] = ""
		if 'location' not in event:
			event['location'] = ""
		if 'location_url' not in event:
			event['location_url'] = ""
		events.append(eventObj(
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
