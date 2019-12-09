import json
import requests
from pandas import DataFrame

classes_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/structure/classes.py').text
exec(classes_txt)
constants_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/master/scripts/constants.py').text
exec(constants_txt)


def rm_main(JSONstring):
	events = json.loads(JSONstring)

	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/output/UNIFIED.json', 'w') as outfile:
		json.dump(events, outfile, indent='\t')

	event_types = [general, science, visual, music, screen, theatre, talk]
	for t in event_types:
		if len(events[t]) > 0:
			events[t] = DataFrame(events[t])
		else:
			fields = [f'GEN_{v}' for v in list(GeneralEvent("", "", "", "", "", "", "", "").keys())[:-1]]
			events[t] = DataFrame(columns=fields)

	events['facilities'] = DataFrame(events['facilities'])
	events[creative_movies] = DataFrame(events[creative_movies])

	#  events[science]
	#   events[visual], events[music], events[screen], events[theatre], events[talk], events['facilities'], events[creative_movies]

	# for k, v in events.items():
	# 	# save single file
	# 	with open(f'C:/Users/andre/Desktop/kdi/scraping/KDI/output/{k}.json', 'w') as outfile:
	# 		json.dump(v, outfile, indent='\t')

	# 	# convert to DF for output
	# 	if len(events[general]) > 0:
	# 		events[k] = DataFrame(v)
	# 	else:

	return events[general], events[science], events[visual], events[music], events[screen], events[theatre], events[talk], events['facilities'], events[
	    creative_movies]
