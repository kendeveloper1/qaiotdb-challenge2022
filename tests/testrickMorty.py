import requests
from assertpy.assertpy import assert_that

#from TF.rickMorty import response


class TestRickMorty():

    def test_status(self):
        newUrl = "https://rickandmortyapi.com/api/character/?name=Pickle Rick"
        payload = {}
        headers = {}
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        assert_that(response.status_code).is_equal_to(200)

    def test_body(self):
        newUrl = "https://rickandmortyapi.com/api/character/?name=Pickle Rick"
        payload = {}
        headers = {}
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        assert_that(response.json()).is_not_empty()

    def test_Character(self):
        newUrl = "https://rickandmortyapi.com/api/character/?name=Pickle Rick"
        payload = {}
        headers = {}
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        assert_that(response.json()['results'][0]).contains('type')
        assert_that(response.json()['results'][0]['type']).is_equal_to('Pickle')

    def test_location(self):
        newUrl = "https://rickandmortyapi.com/api/character/?name=Pickle Rick"
        payload = {}
        headers = {}
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        assert_that(response.json()['results'][0]['location']).contains('name')
        assert_that(response.json()['results'][0]['location']['name']).is_equal_to('Earth (Replacement Dimension)')

    def test_episode(self):
        newUrl = "https://rickandmortyapi.com/api/character/?name=Pickle Rick"
        payload = {}
        headers = {}
        response = requests.request("GET", newUrl, headers=headers, data=payload)
        assert_that(response.json()['results'][0]['episode']).contains('https://rickandmortyapi.com/api/episode/24')








