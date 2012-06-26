#!/usr/bin/env python

"""
Unittest for the config-settings
"""

from nose.tools import assert_equal

from nordnet.config import NordnetConfig

config = NordnetConfig()

def test_username():
    """ Testing the username """
    pass

def test_password():
    """ Testing the password """
    pass

def test_service():
    """ Testing the servicename """
    assert_equal(config.service, 'NEXTAPI')

def test_url():
    """ Testing url name """
    assert_equal(config.url, 'api.test.nordnet.se')
    
def test_base_url():
    """ Testing base url """
    assert_equal(config.base_url, 'api.test.nordnet.se/next')

def test_api_version():
    """ Testing the api version """
    assert_equal(config.api_version, '1')

def test_keys():
    """ Testing the keys folder """
    keys = config.key_path
    print keys

def test_keyfile():
    """ Testing the key-file """
    keyfile = config.public_key
    print keyfile
