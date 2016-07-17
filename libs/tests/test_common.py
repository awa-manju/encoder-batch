import unittest
from libs.common import ls_files


class TestCommon(unittest.TestCase):

    def test_ls_files(self):
        files = ls_files('/tmp', recursive=True)
        print(files)


if __name__ == '__main__':
    unittest.main()
