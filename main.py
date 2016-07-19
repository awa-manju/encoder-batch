#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import glob
import subprocess

# Python スクリプト実行
# 2:00~6:00まで5分毎


recording_dir = '/mnt/videos/recording'
recording_suffix = '.m2ts'
encoding_dir = '/mnt/videos/encoding'
encording_suffix = '.m2ts'

lockfile_comskip = '/tmp/comskip.lock'
lockfile_encode = '/tmp/ffmpeg_encode.lock'

batch_comskip = os.path.join(os.path.dirname(__file__), "comskip.sh")
batch_encode = os.path.join(os.path.dirname(__file__), "encode.sh")

with open('/home/yuta/chinachu/data/recording.json', 'r') as f:
    jsonstr = f.read()
    if not '[]' in jsonstr:
        print('exit')
        exit()


ignore_comskip_strs = [
        'GR26',
        'GR27'
        ]

os.path.exists(lockfile_comskip)

def lockfile_exists(lockfile):
    if os.path.exists(lockfile):
        print("lockfile {} exists.".format(lockfile))
        return True
    else:
        return False

def execute_and_exit(batch, filename, lockfile):
    if not lockfile_exists(lockfile):
        subprocess.call([batch, filename])
        exit()

def ls_files(dirname, suffix):
    files = glob.glob(os.path.join(dirname, '*' + suffix))
    return files

def move_ignore_files(files, ignore_strs, dest_dir):
    for f in files:
        for s in ignore_strs:
            if s in f:
                shutil.move(f, dest_dir)


if __name__ == '__main__':
    if lockfile_exists(lockfile_encode):
        exit()
    if lockfile_exists(lockfile_comskip):
        exit()

    enc_files = ls_files(encoding_dir, encording_suffix)
    if len(enc_files) > 0:
        execute_and_exit(batch_encode, enc_files[0], lockfile_encode)

    rec_files = ls_files(recording_dir, recording_suffix)
    move_ignore_files(rec_files, ignore_comskip_strs, encoding_dir)
    if len(rec_files) > 0:
        execute_and_exit(batch_comskip, rec_files[0], lockfile_comskip)
