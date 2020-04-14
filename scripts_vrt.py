from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

def parse_url(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page, 'html.parser')
    return soup

def find_serie(search_input):
    url = "https://www.vrt.be/vrtnu/a-z/#searchtype=programs"
    soup = parse_url(url)
    
    list_with_available_series = []
    available_series = soup.find_all("h3",{"class":"title"})
    for serie in available_series:
        list_with_available_series.append(serie.text.strip())

    list_with_found_series = []
    for serie in list_with_available_series:
        if search_input.lower() in serie.lower():
            list_with_found_series.append(serie)

    return list_with_found_series


def print_available_series():
    list_with_found_series = find_serie(search_input)
    counter = 0
    for serie in list_with_found_series:
        counter +=  1
        print("--- "+str(counter) + "  " + serie)


def choose_serie(chosen_serie):
    url = "https://www.vrt.be/vrtnu/a-z/#searchtype=programs"
    soup = parse_url(url)

    list_with_found_series = find_serie(search_input)

    serie_a = soup.find("a", text=list_with_found_series[chosen_serie - 1])
    serie_href = "https://www.vrt.be" + serie_a["href"]

    return serie_href


def find_seasons():
    url = choose_serie(chosen_serie)
    soup = parse_url(url)

    seizoenen = soup.find_all("li", {"class":"vrt-labelnav--item"})
    return seizoenen


def print_available_seasons():
    seizoenen = find_seasons()
    lijst = []
    for seizoen in seizoenen:
        lijst.append("Seizoen " + seizoen.text.strip())
    lijst.sort()
    for element in lijst:
        print("--- " + element)
    #print('\n '.join(map(str, lijst)))


def choose_season(chosen_season):
    seizoenen = find_seasons()
    for seizoen in seizoenen:
        if chosen_season == seizoen.text.strip():
            a = seizoen.find('a')
            parameter = a['href']

    url = choose_serie(chosen_serie)
    serie_naam = url.replace('https://www.vrt.be/vrtnu/a-z/','')
    serie_naam = serie_naam.replace('.relevant/','')

    if parameter == '#':
        parameter = '/vrtnu/a-z/' + serie_naam + '/' + chosen_season + '.lists.all-episodes/'
        return "https://www.vrt.be" + parameter
    else:
        return "https://www.vrt.be" + parameter