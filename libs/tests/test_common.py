import unittest
from libs.common import ls_files, any_file_exists


class TestCommon(unittest.TestCase):

    def test_ls_files(self):
        files1 = ls_files('/tmp', recursive=True)
        print(files1)
        files2 = ls_files('/tmp', suffix='.py', recursive=True)
        print(files2)

    def test_any_file_exists(self):
        self.assertEqual(True, any_file_exists(['/tmp', '/etc']))
        self.assertEqual(True, any_file_exists(['/tmp', '/etcc']))
        self.assertEqual(False, any_file_exists(['/tmpp', '/etcc']))
        self.assertEqual(True, any_file_exists(['/tmp']))
        self.assertEqual(False, any_file_exists(['/tmpp']))


if __name__ == '__main__':
    unittest.main()
