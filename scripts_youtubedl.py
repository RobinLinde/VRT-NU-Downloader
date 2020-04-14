from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
import youtube_dl
import scripts_vrt as s
import os

def download_serie():
    url = s.choose_season(s.chosen_season)
    soup = s.parse_url(url)
    
    for link in soup.findAll('a'):
        link = link.get('href')
        link = "https://www.vrt.be" + link
        
        soup = s.parse_url(link)

        aflevering = soup.find('li', attrs={'class': 'episode'})
        aflevering = aflevering.text.strip()
        aflevering = aflevering[4:6]
        beschrijving = soup.find('section', attrs={'class': 'short-description'})
        beschrijving = beschrijving.text.strip()

        list_with_found_series = s.find_serie(s.search_input)
        folder_name = list_with_found_series[s.chosen_serie - 1]

        if len(s.chosen_season) == 2 and len(aflevering) == 2:
            filename = "S" + s.chosen_season + "E" + aflevering.strip() + " " + beschrijving
            folder_name += " S" + s.chosen_season
        elif len(s.chosen_season) == 1 and len(aflevering) == 2:
            filename = "S0" + s.chosen_season + "E" + aflevering.strip() + " " + beschrijving
            folder_name += " S0" + s.chosen_season
        elif len(s.chosen_season) == 2 and len(aflevering) == 1:
            filename = "S" + s.chosen_season + "E0" + aflevering.strip() + " " + beschrijving
            folder_name += " S" + s.chosen_season
        else:
            filename = "S0" + s.chosen_season + "E0" + aflevering.strip() + " " + beschrijving
            folder_name += " S0" + s.chosen_season
        
        print("*************************************************")
        print("Downloading: " + filename)
        
        if os.path.isfile('./' + filename) is False:
            try:
                os.mkdir(folder_name)
            except OSError:
                pass

        with youtube_dl.YoutubeDL({'outtmpl': folder_name + "/" + filename}) as ydl:
            ydl.download([link])

