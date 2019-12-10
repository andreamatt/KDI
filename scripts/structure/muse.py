import json
import requests

utils_txt = requests.get('https://raw.githubusercontent.com/andreamatt/KDI/all_fields/utils/utils.py').text
exec(utils_txt)


def rm_main(JSONString):
	with open('C:/Users/andre/Desktop/kdi/scraping/KDI/DBG/structure.json', 'w') as outfile:
		json.dump(json.loads(JSONString), outfile, indent="\t")

	muse = json.loads(JSONString)
	events = {}

	for e in muse['events']:
		gen = GeneralEvent(e['name'], e['cost'], e['description'], e['link'], '', '', '', e['where'])

		schedule = Schedule([], [], [], '', '')
		if len(e['days']) > 0:
			schedule = Schedule(e['days'], '', '', '', 'daily')

		times = []
		for time in e['time']:
			if '-' in time:
				times.append(DateTime('', '', time.split('-')[0], time.split('-')[1]))
			else:
				times.append(DateTime('', '', time, ''))

		if len(times) == 0:
			times.append(DateTime('', '', '', ''))

		times_with_dates = []
		for date in e['when']:
			if '-' in date:
				for time in times:
					times_with_dates.append(DateTime(date.split('-')[0], date.split('-')[1], time['startTime'], time['endTime']))
			else:
				for time in times:
					times_with_dates.append(DateTime(date, date, time['startTime'], time['endTime']))

		# found no dates => use simple times
		if len(times_with_dates) == 0:
			times_with_dates = times

		for time in times_with_dates:
			event = {}
			for k, v in gen.items():
				event[f'GEN_{k}'] = v
			for k, v in time.items():
				event[f'DATETIME_{k}'] = v
			for k, v in schedule.items():
				event[f'SCHEDULE_{k}'] = v

			if e['Subcategory'] not in events:
				events[e['Subcategory']] = []
			events[e['Subcategory']].append(event)

	return json.dumps(events)