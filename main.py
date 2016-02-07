#!/usr/bin/python
''' 
									Module 1

	Basic Idea : set the config file with user preferences, such as TV show details.
	Input : Series of inputs which are stored in a json file 
	Output : HTML file for Sid to Parse 

'''
# For all the Json functions 
import json
from helper import getListings

# Read individual Series data
def readSeriesData():
	series = raw_input(">>Enter the TV series:\n--> ").strip()
	listing = getListings(series)
	#TODO *issue solve the sorting problem
	for val in sorted(listing):
		print val + "==>" + listing[val]
	# season = raw_input(">>Enter the season which you're watching:\n--> ").strip()
	episode = raw_input("\n>>Enter the latest episode(NUMBER) you saw:\n--> ").strip()
	# quality = raw_input("\n>>Enter the quality of episode(NUMBER) you saw:\n--> ").strip()
	# TODO add download quality
	return { 'series': series, 'episode': "Episode " + episode, 'season': listing['season']}



# Store all the config data in json format to the disk
def readConfigData():
	allSeries = {}
	temp = {}

	while (raw_input(">>Add TV shows?(y/n)").strip()).lower() == 'y':
		temp = readSeriesData()
		allSeries[temp['series']] = temp 	

	configJson = {
		'allSeries': allSeries, 
		'emailRem' : 'n',
	}

	emailRem = (raw_input(">>Would you like email reminders for new episode releases?(y/n) :\n--> ").strip()).lower()
	if emailRem == 'y':
		email = raw_input(">>Enter your email:\n--> ").strip()
		configJson['email'] = email
		configJson['emailRem'] = emailRem

	

	configJson = json.dumps(configJson)

	with open('ConfigFile.txt', 'w') as outfile:
		json.dump(configJson, outfile, sort_keys = False, indent = 4, ensure_ascii=False)	

	return configJson
	# return allSeries, emailRem, email


def readFromConfigFile():
	with open("ConfigFile.txt", 'r') as configFile:
		data = json.loads(configFile.read())

	return data




# print readFromConfigFile()
# compareAndCheckForEpisodes()	
# Print to terminal/console 
print readConfigData()
# getListings()

