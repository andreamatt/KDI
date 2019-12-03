import json
import requests
import pandas as pd


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
	cultura = json.loads(JSONString)
	events = []
	for day in cultura['result']['events']:
		for eventType in day['tipo_evento']:
			for event in eventType['events']:
				subSubCategory = ""
				for subType in event['tipo_evento']:
					if subType['name'] is not None:
						subSubCategory += subType['name'] + ","
				if len(event['luogo_della_cultura']) == 0:
					event['luogo_della_cultura'].append({
						"name": ""
					})
				events.append(eventObj(
						source="cultura",
						category="Cultural",
						subCategory=eventType['name'],
						subSubCategory=subSubCategory,
						title=event['name'],
						link=event['href'],
						date=day['day']['identifier'],
						time=event['orario_svolgimento'],
						locationName=event['comune'][0]['name'] + " --SELF-- " + event[
							'luogo_svolgimento'] + " --SELF-- " +
									 event['luogo_della_cultura'][0]['name'],
						cost=event['costi'],
						contact=event['contact'],
						description=event['description']
				))
	events = [ob.__dict__ for ob in events]
	df = pd.DataFrame(events)
	return df
