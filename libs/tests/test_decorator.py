import unittest
from libs.decorator import LockfileManager, lockfile_manager


class TestLockfileManager(unittest.TestCase):

    def setUp(self):
        self.lockfile = '/tmp/test.lock'
        self.manager = LockfileManager(self.lockfile)

    def test_create_lockfile(self):
        self.manager.create_lockfile()
        self.assertEqual(self.manager.lockfile_exists(), True)

    def test_delete_lockfile(self):
        self.manager.create_lockfile()
        self.manager.delete_lockfile()
        self.assertEqual(self.manager.lockfile_exists(), False)


class TestLockFileManagerDecorator(unittest.TestCase):

    def setUp(self):
        self.lockfile = '/tmp/test.lock'
        self.manager = LockfileManager(self.lockfile)

    def test_create_succuess(self):
        @lockfile_manager(self.lockfile)
        def hello():
            self.assertEqual(self.manager.lockfile_exists(), True)
            print('hello')
        hello()
        self.assertEqual(self.manager.lockfile_exists(), False)

    def test_lockfile_already_exists(self):
        self.manager.create_lockfile()

        @lockfile_manager(self.lockfile)
        def hello():
            print('hello')
        with self.assertRaises(RuntimeError):
            hello()
        self.assertEqual(self.manager.lockfile_exists(), True)
        self.manager.delete_lockfile()
        self.assertEqual(self.manager.lockfile_exists(), False)


if __name__ == '__main__':
    unittest.main()
