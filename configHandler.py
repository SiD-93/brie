#!/usr/bin/env python2
import requests, json, os

# Skeleton structure of the configuration file.
config = {
'quality': '',
'shows': [],
}

l = {
'name': '',
'season': '',
'lastWatched': ''
}

home = os.environ['HOME']
confDir = home + '/.config/brie'

def adder():
    n = raw_input('Enter show name: ')
    l['name'] = n
    s = input('Enter season: ')
    l['season'] = s
    last = input('Enter the last episode you watched: ')
    l['lastWatched'] = last
    return l

def writer(confDict):
    with open(confDir+'/config.json', 'w') as f:
        json.dump(confDict, f, indent=1)
        f.close()

def firstConfig():
    qual = input('Enter the default quality of episodes: ')
    config['quality'] = qual
    config['shows'].append(adder())
    writer(config)

def append():
    with open(confDir+'/config.json', 'r') as f:
        config = json.load(f)
        config['shows'].append(adder())
        writer(config)


def main():
    if not os.path.exists(confDir):
        os.makedirs(confDir)

    if (os.path.exists(confDir+'/config.json')) == False:
        firstConfig()
    else:
        append()

main()


#show = 'silicon valley'
#payload = {'q': show}
#searchBase = 'http://api.tvmaze.com/singlesearch/shows'
#showData = requests.get(searchBase, params=payload)
#print (type(showData.json()))
#showID = str(showData.json()['id'])
#episodesList = requests.get('http://api.tvmaze.com/shows/'+showID+'/episodes')
#print('http://api.tvmaze.com/shows/'+showID+'/episodes')
#print (episodesList.json()[0]['season'])
#print (episodesList.json()[0]['name'])
#print shows['id']
