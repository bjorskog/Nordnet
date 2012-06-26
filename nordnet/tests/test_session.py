#!/usr/bin/env python

""" 
Unit tests for all session-related stuff
"""

from nordnet.restsession import *

def test_make_hash():
    """ Testing to make a hash-key """
    hashkey = make_hash()
    print hashkey

def test_connect():
    """ Connecting to the HTTP server """
    connection = connect()

def test_login():
    """ Loggon to the HTTP server """
