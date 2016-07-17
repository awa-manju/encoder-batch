import unittest
import datetime
from libs.comskip import ComskipBatchWrapper


class TestComskipBatchWrapper(unittest.TestCase):

    def setUp(self):
        self.comskip = ComskipBatchWrapper()

    def test_update_timestamp(self):
        filename = '/tmp/test.ts'
        timestamp = self.comskip._get_timestamp(filename)
        self.comskip._update_timestamp(filename, timestamp)

    def test_create_cmd(self):
        cmd_opt = self.comskip._create_cmd_opt({
                'margin': 3, 'filename': '/tmp/test.ts',
                'move_to': '/tmp/videos', 'failed_to': '/tmp/videos/archive'})
        self.assertListEqual(sorted(cmd_opt[::2]), [
            '--failed_to', '--filename', '--margin', '--move_to'])


if __name__ == '__main__':
    unittest.main()
