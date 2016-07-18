import os
import subprocess
from abc import ABCMeta, abstractmethod
from glob import glob


def any_file_exists(files):
    for fl in files:
        if os.path.exists(fl):
            return True
    return False


def ls_files(dirname, prefix='*', suffix='.*', recursive=False):
    recursivedir = '**' if recursive else ''
    path = os.path.join(dirname, recursivedir, prefix + suffix)
    return glob(path, recursive=recursive)


def get_timestamp(filename):
    return os.stat(filename).st_mtime


def update_timestamp(filename, timestamp):
    os.utime(filename, (timestamp, timestamp))


def copy_timestamp(beforefile, afterdir=None, afterfile=None):
    if afterdir is None and afterfile is None:
        raise TypeError('afterdir or afterfile must be set.')
    elif afterfile is None:
        afterfile = os.path.join(afterdir, os.path.basename(beforefile))

    timestamp = get_timestamp(beforefile)
    update_timestamp(afterfile, timestamp)


class Base(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, filename):
        pass

    def _create_cmd_opt(self, cmd_dic):
        cmd_opt = []
        for k, v in cmd_dic.items():
            if len(k) == 1:
                cmd_opt.append('-'+k)
            else:
                cmd_opt.append('--'+k)
            cmd_opt.append(v)
        return cmd_opt

    def _execute_cmd(self, cmd, opt):
        # execute command
        full_cmd = opt[:]
        full_cmd.insert(0, cmd)
        print(' '.join(full_cmd))
        subprocess.run(full_cmd)
