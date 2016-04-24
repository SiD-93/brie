#!/usr/bin/env python2
import requests, json

show = 'silicon valley'
payload = {'q': show}
searchBase = 'http://api.tvmaze.com/singlesearch/shows'
showData = requests.get(searchBase, params=payload)
#print (type(showData.json()))
showID = str(showData.json()['id'])
episodesList = requests.get('http://api.tvmaze.com/shows/'+showID+'/episodes')
#print('http://api.tvmaze.com/shows/'+showID+'/episodes')
print (episodesList.json()[0]['season'])
print (episodesList.json()[0]['name'])
#print shows['id']
#with open('./show.json', 'w') as f:
#	json.dump(r.json(), f, indent=1)
#	f.close()
