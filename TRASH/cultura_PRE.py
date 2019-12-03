import json
import requests
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
import urllib.request
import cloudpickle as cp

test = []


def rm_main():
	url = 'http://194.32.77.99/KDI/dataset/cultura.json'
	cultura = json.loads(requests.get(url).text)
	for day in cultura['result']['events']:
		for eventType in day['tipo_evento']:
			for event in eventType['events']:
				eventId = event['main_node_id']
				# if eventId not in test:
				# 	test.append(eventId)
				# else:
				# 	print(eventId)
				# 	continue
				# url = "https://www.cultura.trentino.it/eng/content/view/full/"+str(eventId)
				# chromeOptions = webdriver.ChromeOptions()
				# chromeOptions.add_argument("--no-sandbox")
				# chromeOptions.add_argument("--disable-dev-shm-using")
				# chromeOptions.add_argument("--start-maximized")
				# chromeOptions.add_argument("--headless")
				# driver = webdriver.Chrome(options=chromeOptions)
				# driver.get(url)
				# content = driver.page_source
				# with open('cultura_Pages/cultura_'+str(eventId)+'_page.pkl', 'wb') as f:
				# 	pickle.dump(content, f)
				url = 'http://arya.li/KDI/cultura_Pages/cultura_' + str(eventId) + '_page.pkl'
				urllib.request.urlretrieve(url, 'objs.pkl')
				with open('objs.pkl', 'rb') as f:
					content = pickle.load(f)
					
				HTMLPage = BeautifulSoup(content, "html.parser")
				
				mainBody = HTMLPage.find(class_="content-main")
				descriptions = mainBody.find(class_="descrizione").find_all("p")
				description = ""
				for section in descriptions:
					description += section.get_text()
				event['description'] = description
				
				sidebar = HTMLPage.find(class_="content-related")
				contacts = sidebar.find_all(class_="list-group-item")
				contact = ""
				for item in contacts:
					item.find("i").decompose()
					contact += item.get_text()
				event['contact'] = description
			
	return json.dumps(cultura)


culturaJSON = rm_main()
