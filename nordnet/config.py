#!/usr/bin/env python

""" 
Module for managing all config-properties and logging
"""

import logging
from ConfigParser import ConfigParser
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
    return logger
    
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
        """ Getter for password """
        return self._get_field('Session', 'password')
    
    @property
    def service(self):
        """ Getter for servicename """
        return self._get_field('Session', 'service')
    
    @property
    def url(self):
        """ Getter for url """
        return self._get_field('Session', 'url')

    @property
    def base_url(self):
        """ Getter for the base url """
        return self._get_field('Session', 'base_url')
    
    @property 
    def api_version(self):
        """ Getter for api-version """
        return self._get_field('Session', 'api_version')

    @property
    def key_path(self):
        """" Getter for the path to all keys """
        keypath = self._get_field('System', 'keypath')
        localpath = "/".join(__file__.split('/')[:-1])
        return join(localpath, keypath)

    @property
    def public_key(self):
        """ Getter for the file to the key-file """
        keyfile = self._get_field('System', 'keyfile')
        return join(self.key_path, keyfile)
