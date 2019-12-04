import json
import pandas as pd
import requests


def GeneralEvent(name, price, description, website, duration, language, isTicketAvailable, locationText):
	return locals()


def ScienceEvent(topic):
	return locals()


def VisualArtsEvent(artMovement):
	return locals()


def MusicEvent(genre, performer):
	return locals()


def ScreeningEvent(salaNumber):
	return locals()


def TheatreEvent(interpreters):
	return locals()


def TalkEvent(hasPresentation, isConference):
	return locals()


def VisualArtwork(style):
	return locals()


def MusicPlaylist(songs):
	return locals()


def Movie(originalName, genre, duration):
	return locals()


def Play(genre):
	return locals()


def Book(pages, genre, editor):
	return locals()


def Time(startDate, endDate, startTime, endTime):
	return locals()


def Period(byDay, byMonth, byMonthDay, repeatCount, repeatFrequency):
	return locals()


def Discount(young, students, children, groups):
	return locals()


def CreativeWork(name, creator, createDate, url):
	return locals()


def Facility(name, telephone, website, mail, hasParking, animalsAllowed, smokingAllowed, isIndoor):
	return locals()


def Timetables(monday, tuestay, wednesday, thursday, friday, saturday, sunday):
	return locals()


def GeoCoordinates(latitude, longitude, altitude, address, addressLocality, addressRegion, postalCode, locationText):
	return locals()


classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONString):
	trentoTodayE = json.loads(JSONString)
	events = {}

	for e in trentoTodayE:
		gen = GeneralEvent(e['Title'], e['price'], e['description'], e['Link'], '', '', '', e['location'])
		time = Time(e['startDate'], e['endDate'], e['startTime'], e['endTime'])
		event = {**gen, **time}

		if e['category'] not in events:
			events[e['category']] = []
		events[e['category']].append(event)

	#events = [ob.__dict__ for ob in events]
	#df = pd.DataFrame(events)
	#return df

	return json.dumps(events)
