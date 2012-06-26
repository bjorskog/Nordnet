#!/usr/bin/env python

""" 
Class for managing all config-properties
"""

import logging
import ConfigParser
from os.path import dirname, join

CONFIG_FILE = 'nordnet.cfg'
CONFIG_FILE_PATH = dirname(__file__)
CONFIG = join(CONFIG_FILE_PATH, CONFIG_FILE)

LOG_FILE = 'nordnet.log'
LOG = join(CONFIG_FILE_PATH, LOG_FILE)

def get_logger():
    logger = logging.getLogger('nordnet-api')
    logger.setLevel(logging.DEBUG)
    
    filehandler = logging.FileHandler(LOG)
    filehandler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

class NordnetConfig(object):
    """ Config-class for the config """
    
    def __init__(self):
        self._configparser = ConfigParser()
        self._configparser.read(CONFIG)

    def _get_field(self, section, field):
        """ Generic method to get a field """
        if not self._configparser.has_option(section, field):
            return None
        return self._configparser.get(section, field).strip()

    @property
    def username(self):
        """ Getting the username """
        return self._get_field('Session', 'username')

    @property
    def password(self):
        """ Getting the password """
        return self._get_field('Session', 'password')
