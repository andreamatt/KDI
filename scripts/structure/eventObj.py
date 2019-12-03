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
