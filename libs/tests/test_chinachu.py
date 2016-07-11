import unittest
from chinachu import ChinachuClient


class TestChinachuClient(unittest.TestCase):

    base_url = 'http://192.168.0.122'
    port = 10772
    auth = ('akari', 'bakuhatsu')
    client = ChinachuClient(base_url, port, auth)

    def test_reserves(self):
        print(self.client.reserves.list()[0]['end'])

    def test_recorded(self):
        print(self.client.reserves.list())

if __name__ == '__main__':
    unittest.main()
