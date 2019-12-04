import json
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

api_key = 'AIzaSyDLEU6MpVGA5Pi4Kh44p7Jmt_nkAWY8kbE'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
outputArray = []


def substring(string):
    substring = string.replace("V.O. ", "")
    substring = re.sub("[\(\[].*?[\)\]]", "", substring)

    return substring


def findMovie(json):
    for item in json["itemListElement"]:
        for element in item["result"]["@type"]:
            if element == "Movie":
                if 'detailedDescription' in item['result']:
                    return item['result']['detailedDescription']['url']

    return False


def exploreGraph(query):
    params = {
        'query': query,
        'limit': 10,
        'indent': True,
        'key': api_key,
        'languages': 'it',
    }

    url = service_url + '?' + urllib.parse.urlencode(params)
    response = json.loads(urllib.request.urlopen(url).read())
    wikiUrl = findMovie(response)

    if not wikiUrl:
        paramsUp = {'query': query.lower()}
        params.update(paramsUp)
        url = service_url + '?' + urllib.parse.urlencode(params)
        response = json.loads(urllib.request.urlopen(url).read())
        wikiUrl = findMovie(response)
        print(query.lower())
    else:
        print(query)

    return wikiUrl


def parse(url):
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')

    title = standardFind(soup, "Titolo originale")
    country = standardFind(soup, "Paese di produzione")
    year = standardFind(soup, "Anno")
    company = listFind(soup, "Casa di produzione")
    lenght = nonStandardFind(soup, "Durata")
    language = nonStandardFind(soup, "Lingua originale")
    genreList = listFind(soup, "Genere")
    directorList = listFind(soup, "Regia")

    new_dict = {
        'original title': title,
        'country': country,
        'year': year,
        'company': company,
        'lenght': lenght,
        'language': language,
        'genre': genreList,
        'director': directorList
    }

    return new_dict


def standardFind(soup, tag):
    found = soup.find(text=tag)
    if found:
        print(found)
        return found.parent.parent.findNext(
            'td').contents[0].text


def nonStandardFind(soup, tag):
    found = soup.find(text=tag)
    if found:
        print(found)
        return found.parent.parent.findNext(
            'a').text


def listFind(soup, tag):
    found = soup.find(text=tag)
    if found:
        obj = found.parent.parent.findNext('td')
        array = [x.text for x in obj.find_all('a')]
        return array


with open('cineworldTrento.json', 'r') as fp:
    obj = json.load(fp)

moviesArray = obj["movies"]
for movie in moviesArray:
    title = movie["title"]
    query = substring(title)
    url = exploreGraph(query)
    movieDict = {
        'title': title,
        'wikiUrl': url
    }
    if url:
        print(url)
        new_dict = parse(url)
        movieDict.update(new_dict)

    outputArray.append(movieDict)


with open('graph.json', 'w', encoding='utf-8') as f:
    json.dump(outputArray, f, ensure_ascii=False, indent=4)
