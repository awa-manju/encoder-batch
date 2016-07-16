import os
import subprocess
from libs.config import Config
from libs.decorator import lockfile_manager

config = Config().comskip
lock_file = config['lock_file']


def comskip_execute(filename):
    comskip = ComskipBatchWrapper()
    comskip.execute(filename)


class ComskipBatchWrapper:

    def __init__(self):
        self.cmd = config['cmd']
        self.dest_dir = config['dest_dir']
        self.backup_dir = config['backup_dir']

    @lockfile_manager(lock_file)
    def execute(self, filename):
        timestamp = self._get_timestamp(filename)
        cmd_opt = self._create_cmd_opt(
                margin=3, filename=self.filename,
                move_to=self.dest_dir, failed_to=self.backup_dir)
        self._execute_cmd(self.cmd, cmd_opt)
        moved_file = os.path.join(self.dest_dir, os.path.basename(filename))
        self._update_timestamp(moved_file, timestamp)

    def _get_timestamp(self, filename):
        return os.stat(filename).st_mtime

    def _create_cmd_opt(
            self, margin=3, filename=None, move_to=None, failed_to=None):
        # cmd opt
        cmd_opt = []
        cmd_opt.append('--margin')
        cmd_opt.append(margin)
        cmd_opt.append('--file')
        cmd_opt.append(filename)
        cmd_opt.append('--move_to')
        cmd_opt.append(move_to)
        cmd_opt.append('--failed_to')
        cmd_opt.append(failed_to)
        return cmd_opt

    def _execute_cmd(self, cmd, opt):
        # execute command
        full_cmd = opt[:]
        full_cmd.insert(0, cmd)
        subprocess.call(full_cmd)

    def _update_timestamp(self, filename, timestamp):
        # mod timestamp
        os.utime(filename, (timestamp, timestamp))
