import datetime
import requests


class Base:

    _api_url = '/api'
    _json_format = '.json'
    resource_url = None

    def __init__(self, base_url, auth):
        self.url = base_url + self._api_url + self.resource_url
        self.auth = auth

    def list(self, sort_key=None):
        response = requests.get(self.url + self._json_format, auth=self.auth)
        result = response.json()
        if sort_key is not None:
            result = sorted(result, key=self._key_cmp(sort_key))
        return result

    def _to_datetime(self, unixtime_milli):
        unixtime_sec = int(int(unixtime_milli) / 1000)
        return datetime.datetime.fromtimestamp(unixtime_sec)

    def _key_cmp(self, key):
        def __key_cmp(x):
            if key == 'start' or 'end':
                return self._to_datetime(x[key])
            print(x, key)
            return x
        return __key_cmp


class Reserves(Base):

    resource_url = '/reserves'

    def vacant_time(self):
        first_reserve = self.list(sort_key='start')[0]
        now = datetime.datetime.now()
        vtime = self._to_datetime(first_reserve['start']) - now
        zerotime = datetime.timedelta(0)
        if vtime > zerotime:
            return vtime
        else:
            return zerotime


class Recorded(Base):

    resource_url = '/recorded'


class Recording(Base):

    resource_url = '/recording'

    def is_busy(self):
        return len(self.list()) != 0
