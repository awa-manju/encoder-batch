import unittest
from libs.chinachu import ChinachuClient


class TestChinachuClient(unittest.TestCase):

    base_url = 'http://192.168.0.122'
    port = 10772
    auth = ('akari', 'bakuhatsu')
    client = ChinachuClient(base_url, port, auth)

    def test_reserves(self):
        result = list(self.client.reserves.list()[0].keys())
        keys = ['detail', 'seconds', 'end', 'title', 'episode', 'channel',
                'fullTitle', 'isConflict', 'category', 'id', 'flags',
                'isManualReserved', 'subTitle', 'start']
        self.assertListEqual(sorted(result), sorted(keys))

    def test_recorded_sort_by_datetime_key(self):
        key = 'start'
        result = self.client.reserves.list(sort_key=key)
        for i, v in enumerate(result):
            if i > 0:
                a = result[i-1][key]
                b = result[i][key]
                self.assertLessEqual(int(a), int(b))

    def test_get_vacant_time(self):
        # print(self.client.reserves.vacant_time())
        pass

    def test_is_recording(self):
        # print(self.client.recording.is_busy())
        pass

if __name__ == '__main__':
    unittest.main()
