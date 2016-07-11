import requests


class Base:

    _api_url = '/api'
    _json_format = '.json'
    resource_url = None

    def __init__(self, base_url, auth):
        self.url = base_url + self._api_url + self.resource_url
        self.auth = auth

    def list(self):
        response = requests.get(self.url + self._json_format, auth=self.auth)
        return response.json()


class Reserves(Base):

    resource_url = '/reserves'


class Recorded(Base):

    resource_url = '/recorded'
