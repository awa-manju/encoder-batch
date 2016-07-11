from client import Reserves, Recorded


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
