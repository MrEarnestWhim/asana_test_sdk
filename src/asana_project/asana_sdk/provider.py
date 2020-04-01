import requests
from django.conf import settings


class AsanaCore(object):
    def __init__(self):
        self._token = settings.PERSONAL_ACCESS_TOKEN
        self._version = '1.0'
        self._url = 'https://app.asana.com/api/'

    @property
    def __headers(self):
        return {
            'authorization': f'Bearer {self._token}',
            'accept': 'application/json',
            'content-type': 'application/json'
        }

    def url_compile(self, url):
        return f'{self._url}{self._version}{url}'

    def post(self, url: str, params=None) -> dict:
        if params is None:
            params = {}

        response = requests.post(
            self.url_compile(url),
            headers=self.__headers,
            json={'data': params}
        )
        return response.json()

    def put(self, url: str, params=None) -> dict:
        if params is None:
            params = {}

        response = requests.put(
            self.url_compile(url),
            headers=self.__headers,
            json={'data': params}
        )
        return response.json()

    def get(self, url: str) -> dict:
        response = requests.get(
            self.url_compile(url),
            headers={
                'authorization': f'Bearer {self._token}'
            }
        )
        return response.json()
