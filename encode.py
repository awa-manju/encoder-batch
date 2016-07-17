from libs.common import ls_files
from libs.comskip import comskip_execute
from libs.config import Config

cfg = Config()
config_comskip = cfg.comskip
config_encoder = cfg.encoder


def a_file(dirname):
    files = ls_files(dirname, suffix='.m2ts')
    return files[0]


def main():
    src_dir = config_comskip['src_dir']
    file_for_comskip = a_file(src_dir)
    comskip_execute(file_for_comskip)


if __name__ == '__main__':
    main()
