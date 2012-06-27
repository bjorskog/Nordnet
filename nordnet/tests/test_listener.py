#!/usr/bin/env python

"""
Unit tests for the listeners

"""

import sys

from nordnet.listeners import PublicListener
from nordnet.restsession import *

def test_listener():
    """ Simple entry for tests """
    hashkey = make_hash()
    connection = connect()
    response = login(connection, hashkey)

    session_key = response['session_key']
    hostname = response['public_feed']['hostname']
    port = response['public_feed']['port']

    print 'Opening socket to: %s:%s' % (hostname, port)
    publiclistener = PublicListener(session_key, hostname, port)
    publiclistener.login()
    publiclistener.subscribe(11, 101)
    try:
        publiclistener.start()
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
