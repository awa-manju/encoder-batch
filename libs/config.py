from configparser import ConfigParser
from libs.const import INIFILE


class Config:

    def __init__(self, inifile=INIFILE):
        config = ConfigParser()
        config.read(inifile)
        self.encoder = dict(config.items('encoder'))
        self.comskip = dict(config.items('comskip'))
        self.chinachu = dict(config.items('chinachu'))
