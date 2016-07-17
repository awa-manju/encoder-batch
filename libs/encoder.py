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
        encoded_basefile = basefilename + ext
        cmd_opt_input = self._create_cmd_opt({'i': filename})
        cmd_opt_vsize = self._create_cmd_opt({'s': '1280x720'})
        arg_list = []
        arg_list.extend(cmd_opt_input)
        arg_list.extend(cmd_opt_vsize)
        arg_list.extend([encoded_basefile])
        self._execute_cmd(self.cmd, arg_list)
        copy_timestamp(filename, afterfile=encoded_basefile)
        encoded_srcfile = os.path.join(
                os.path.dirname(filename), os.path.basename(basefilename) + ext)
        encoded_dstfile = os.path.join(
                self.dest_dir, os.path.basename(basefilename) + ext)
        try:
            shutil.move(encoded_srcfile, encoded_dstfile)
        except OSError:
            pass
