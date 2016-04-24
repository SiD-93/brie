#!/usr/bin/env python2
import requests, json

config = {
'quality': '',
'shows': [],
}

qual = input('Enter quality: ')
config['quality'] = qual

def show():
    l = {
    'name': '',
    'season': ''
    }
    n = raw_input('Enter show name: ')
    l['name'] = n
    s = raw_input('Enter season: ')
    l['season'] = s
    print l
    config['shows'].append(l)
show()
show()
print config

with open('./conf.json', 'w') as f:
    json.dump(config, f, indent=1)
    f.close()

#makeConf()
#show = 'silicon valley'
#payload = {'q': show}
#searchBase = 'http://api.tvmaze.com/singlesearch/shows'
#showData = requests.get(searchBase, params=payload)
##print (type(showData.json()))
#showID = str(showData.json()['id'])
#episodesList = requests.get('http://api.tvmaze.com/shows/'+showID+'/episodes')
##print('http://api.tvmaze.com/shows/'+showID+'/episodes')
#print (episodesList.json()[0]['season'])
#print (episodesList.json()[0]['name'])
##print shows['id']
##with open('./show.json', 'w') as f:
##	json.dump(r.json(), f, indent=1)
##	f.close()
