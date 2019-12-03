class Facility:

	def __init__(self, name="", telephone="", website="", mail="", hasParking="", animalsAllowed="", smokingAllowed="", isIndoor=""):
		self.name = name
		self.telephone = telephone
		self.website = website
		self.mail = mail
		self.hasParking = hasParking
		self.animalsAllowed = animalsAllowed
		self.smokingAllowed = smokingAllowed
		self.isIndoor = isIndoor


class GeoCoordinates:

	def __init__(self, latitude="", longitude="", altitude="", address="", addressLocality="", addressRegion="", postalCode=""):
		self.latitude = latitude
		self.longitude = longitude
		self.altitude = altitude
		self.address = address
		self.addressLocality = addressLocality
		self.addressRegion = addressRegion
		self.postalCode = postalCode