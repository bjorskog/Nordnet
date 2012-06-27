#!/usr/bin/env python

"""
Main entry point for the Nordnet application

"""

import threading

from nordnet.listeners import PublicListener
from nordnet.restsession import *

def main():
    """ Simple entry for protyping purposes """
    hashkey = make_hash()
    connection = connect()
    response = login(connection, hashkey)

    session_key = response['session_key']
    hostname = response['public_feed']['hostname']
    port = response['public_feed']['hostname']

    publiclistener = PublicListener()
    publiclistener.setup(session_key, hostname, port)
    publiclistener.login()
    publiclistener.subscribe(11, 101)
    publiclistener.start()

class Controller(threading.Thread):
    """ Controller for managing connections, sockets """

    def __init__(self):
        threading.Thread.__init__(self)
        
    def connect(self):
        """ Connecting to the REST-service """
        pass

    def listen(self):
        """ Start listening """
        pass

    def run(self):
        pass
