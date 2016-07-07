from configparser import ConfigParser
from libs.const import INIFILE


class Config:

    def __init__(self, inifile=INIFILE):
        config = ConfigParser()
        config.read(inifile)
        self.comskip = dict(config.items('comskip'))
        self.encoder = dict(config.items('encoder'))
