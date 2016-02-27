#!/usr/bin/python
''' 
									Module 2

	Basic Idea : Get Details from user set config files and fetch the episode list.
	Input : ConfigJSON file from the localStorage  
	Output : List of EpisodesNumber and EpisodeSNames that needs to be downloaded
'''
import requests 
import re
from bs4 import BeautifulSoup
import os


def getListings(tvShow):
	# tvShow = raw_input(">>Enter the Name of the TV show\n-->")

	link = "http://www.tv.com/shows/" + tvShow + "/episodes/"

	pageData = requests.get(link)

	soup = BeautifulSoup(pageData.content, "lxml")

	lisOfEpisodesName = soup.find_all("a", {"class": "title"})
	lisOfEpisodesNumber = soup.find_all("div", {"class": "ep_info"})
	

	# Fetch the latest season 
	season = soup.find_all("a", {"class": "season_name"})

	for tem in season:
		seasonName  = (str(tem.text)).strip() 
		break
		
	episodeName = []
	episodeNumber = []

	for nameOfEpisode in lisOfEpisodesName:
		episodeName.append(str(nameOfEpisode.text))
		# print nameOfEpisode.text

	for numberOfEpisode in lisOfEpisodesNumber:

		episodeNumber.append((str(numberOfEpisode.text).strip()))
		# print numberOfEpisode.text
	# print lisOfEpisodes

	dictOfEpisodes = {}

	for x in xrange(0, len(episodeNumber)):
		dictOfEpisodes[episodeNumber[x]] = episodeName[x]

	dictOfEpisodes.update({'season': seasonName})

	return dictOfEpisodes



def downloadEpisodes(episodeList):

	for episode in episodeList:
		e = episodeList['arrow']['episode']
		s = episodeList['arrow']['season']
		ser = episodeList['arrow']['series']
		queryString = ser + "-" + "s" + ((s[7]) if int(s[7]) > 10 else ('0' + s[7])) + "e" + ((e[8]) if int(e[8]) > 10 else ('0' + e[8]))	

		download(queryString)





def download(queryString):

	link = "https://eztv.ag/search/" + queryString

	print link

	pageData = requests.get(link)

	soup = BeautifulSoup(pageData.content, "lxml")

	magnetFiles = soup.find_all("a", {"class": "magnet"})

	for magnet in magnetFiles:
		downloadMagnet = magnet.get("href")
		break

	os.startfile(downloadMagnet)
	


