from libs.common import ls_files, any_file_exists
from libs.comskip import comskip_execute
from libs.encoder import encoder_execute
from libs.config import Config

cfg = Config()
config_comskip = cfg.comskip
config_encoder = cfg.encoder


def a_file(dirname):
    files = ls_files(dirname, suffix='.m2ts')
    return files[0] if len(files) else None


def comskip():
    src_dir = config_comskip['src_dir']
    file_for_comskip = a_file(src_dir)
    if file_for_comskip is not None:
        try:
            comskip_execute(file_for_comskip)
        except RuntimeError as e:
            print('{}'.format(e))


def encode():
    src_dir = config_encoder['src_dir']
    file_for_encode = a_file(src_dir)
    if file_for_encode is not None:
        try:
            encoder_execute(file_for_encode)
        except RuntimeError as e:
            print('{}'.format(e))


if __name__ == '__main__':
    lockfiles = [config_comskip['lock_file'], config_encoder['lock_file']]
    if any_file_exists(lockfiles):
        print('lockfile exists...')
        exit()
    encode()
    comskip()
