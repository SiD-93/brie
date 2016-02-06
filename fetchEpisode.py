import requests 
import re
from bs4 import BeautifulSoup


tvShow = raw_input(">>Enter the Name of the TV show\n-->")

link = "http://www.tv.com/shows/" + tvShow + "/episodes/"

pageData = requests.get(link)

soup = BeautifulSoup(pageData.content, "lxml")

lisOfEpisodesName = soup.find_all("a", {"class": "title"})
lisOfEpisodesNumber = soup.find_all("div", {"class": "ep_info"})

episodeName = []
episodeNumber = []

for nameOfEpisode in lisOfEpisodesName:
	episodeName.append(str(nameOfEpisode.text))
	# print nameOfEpisode.text

for numberOfEpisode in lisOfEpisodesNumber:

	episodeNumber.append((str(numberOfEpisode.text).strip()))
	# print numberOfEpisode.text
# print lisOfEpisodes


for x in xrange(0, len(episodeNumber)):
	print episodeNumber[x], "=>", episodeName[x]