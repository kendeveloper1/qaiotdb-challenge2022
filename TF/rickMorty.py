import requests
import pprint
import urllib.parse

baseUrl = "https://rickandmortyapi.com/api"
charactersUrl = "https://rickandmortyapi.com/api/character",
locationUrl = "https://rickandmortyapi.com/api/location",
episodesUrl = " https://rickandmortyapi.com/api/episode"

resp = requests.get(baseUrl)
body = resp.json()
pprint.pprint(body)


def getCharacterInfo():
    resp = requests.get(newUrl).json()['results']
    for x in resp:
        return x.get('species'), x.get('type')


def getLocation():
    return requests.get(newUrl).json()['results'][0]['location']


def getEpisode():
    return requests.get(newUrl).json()['results'][0]['episode']


def get(id=None):
    if id == None:
        print("Id character is requiered.")
        print("use get all to all characters.")
        return
    return requests.get(charactersUrl + str(id)).json()


characterName = input("enter your famous character name example Pickle Rick : ")
str(characterName)
newUrl = "https://rickandmortyapi.com/api/character/?name=" + characterName
print(newUrl)
payload = {}
headers = {}
response = requests.request("GET", newUrl, headers=headers, data=payload)
print('Character info  ->')
pprint.pprint(getCharacterInfo())
print('Location/s info ->')
pprint.pprint(getLocation())
print('Episode/s info  ->')
pprint.pprint(getEpisode())
