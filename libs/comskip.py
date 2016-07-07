from config import Config
from libs.decorator import lockfile_manager

config = Config().comskip
lock_file = config['lock_file']


class ComskipBatchWrapper:

    def __init__(self):
        self.cmd = config['cmd']
        self.dest_dir = config['dest_dir']
        self.backup_dir = config['backup_dir']

    @lockfile_manager(lock_file)
    def execute(self):
        pass
