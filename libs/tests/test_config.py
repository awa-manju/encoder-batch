import unittest
from libs.config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_comskip(self):
        self.assertEqual(self.config.comskip['dest_dir'], '/mnt/videos/encoding')

    def test_encoder(self):
        self.assertEqual(self.config.encoder['dest_dir'], '/mnt/archive/videos/backup')


if __name__ == '__main__':
    unittest.main()
