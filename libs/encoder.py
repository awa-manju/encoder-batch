import os
import shutil
from libs.config import Config
from libs.decorator import lockfile_manager, recording_busy
from libs.common import Base, copy_timestamp

config = Config().encoder
lock_file = config['lock_file']


@recording_busy
def encoder_execute(filename):
    encoder = Encoder()
    encoder.execute(filename)


class Encoder(Base):

    def __init__(self):
        self.cmd = config['cmd']
        self.dest_dir = config['dest_dir']
        self.backup_dir = config['backup_dir']

    @lockfile_manager(lock_file)
    def execute(self, filename):
        basefilename, _ = os.path.splitext(filename)
        ext = '.mp4'
        encoded_file = os.path.join(self.dest_dir, os.path.basename(basefilename) + ext)
        cmd_opt_input = self._create_cmd_opt({'i': filename})
        cmd_opt_vsize = self._create_cmd_opt({'s': '1280x720'})
        arg_list = []
        arg_list.extend(cmd_opt_input)
        arg_list.extend(cmd_opt_vsize)
        arg_list.extend([basefilename + ext])
        self._execute_cmd(self.cmd, arg_list)
        shutil.move(filename, encoded_file)
        copy_timestamp(encoded_file, afterfile=encoded_file)
