#!/home/yuta/.pyenv/shims/python

import sys
import os
import json
import datetime
import uuid
from string import Template


argvs = sys.argv
argc = len(argvs)
if argc < 2:
    print('Usage: python {} [recorded data path] [program data (JSON)]'.format(argvs[0]))
    exit(1)


def to_datetime(unixtime_milli):
    unixtime_sec = int(int(unixtime_milli) / 1000)
    return datetime.datetime.fromtimestamp(unixtime_sec)


recoreded_data_path = argvs[1]
recoreded_data_dir = os.path.dirname(recoreded_data_path)
recoreded_data_name = os.path.basename(recoreded_data_path)
recoreded_data_base, _ = os.path.splitext(recoreded_data_name)

program_data = json.loads(argvs[2])
program_data_timestamp = to_datetime(program_data['start'])

comskipped_data_dstdir = '/mnt/videos/encoding'
comskipped_data_bakcupdir = '/mnt/archive/videos/backup'
comskipped_data_name = recoreded_data_name
comskipped_data_path = os.path.join(comskipped_data_dstdir, comskipped_data_name)

encoded_data_dstdir = '/mnt/archive/videos'
encoded_data_ext = '.mp4'
encoded_data_name = recoreded_data_base + '.mp4'

lockfile = 'ffmpeg_encode.lock'
template_file = os.path.join(os.path.dirname(__file__), 'post_recorded.sh.template')
output_file = os.path.join('/tmp', str(uuid.uuid1()))
renamed_file = os.path.join('/tmp', recoreded_data_base + '.sh')


if __name__ == '__main__':

    with open(template_file, 'r') as inf:
        with open(output_file, 'w') as outf:
            template_str = Template(inf.read())
            outstr = template_str.substitute(
                    COMSKIP_CMD='$COMSKIP_CMD',
                    FFMPEG_CMD='$FFMPEG_CMD',
                    LOCKFILE=lockfile,
                    VIDEOFILE=recoreded_data_path,
                    BASENAME=recoreded_data_base,
                    COMSKIP_DSTDIR=comskipped_data_dstdir,
                    COMSKIP_BACKUPDIR=comskipped_data_bakcupdir,
                    RECORDED_DIR=recoreded_data_dir,
                    PROGRAM_TITLE=program_data['title'],
                    ENCODE_DSTDIR=encoded_data_dstdir,
                    TIMESTAMP=program_data_timestamp,
                    SELFPATH=output_file
                    )
            outf.write(outstr)

    os.rename(output_file, renamed_file)
