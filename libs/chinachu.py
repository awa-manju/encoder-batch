from libs.config import Config
from libs.client import Reserves, Recorded, Recording

config = Config().chinachu


def client():
    return ChinachuClient(
            config['url'], config['port'],
            (config['user'], config['pass']))


class ChinachuClient:

    def __init__(self, base_url, port, auth):
        self.url = base_url + ':' + str(port)
        self.auth = auth

    @property
    def reserves(self):
        return Reserves(self.url, self.auth)

    @property
    def recorded(self):
        return Recorded(self.url, self.auth)

    @property
    def recording(self):
        return Recording(self.url, self.auth)
