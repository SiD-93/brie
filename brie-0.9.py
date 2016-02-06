# Brie.py v0.9 - Simple data scraper written in Python using BeautifulSoup
# and Requests.
# At this version, the scraper works for one site and one show.
import requests # HTTP for Humans :-)

from bs4 import BeautifulSoup # Simple but effective scraper library.

r = requests.get('https://eztv.ag/search/the-flash') # get page.

soup = BeautifulSoup(r.content, "lxml") # using parser lxml.

# these might cause problems if the site is modified even slightly.
fl_name = soup.find_all("a", {"class": "epinfo"})
fl_magnet = soup.find_all("a", {"class": "magnet"})

# simple for loops to obtain the data.
for item in fl_name:
    if "720" in item.text:
        print item.text # print episode name.
for item in fl_magnet:
    if "720" in item.get("title"):
        print item.get("href") # print magnet link.

# To fix : 
# * Prints ALL episodes from page. Option to select episodes.
# * Works for 720p versions, can be tuned according to preferences.
