#!/usr/bin/env python

""" 
Listeners that feed on the stream coming from
the public or private feeds.
"""

import ssl
import socket
import threading
from json import dumps as jdumps

__all__ = ['PublicListener']

class PublicListener(threading.Thread):
    """ Listening to Nordnet on a socket """

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._taskqueue = queue

    def setup(self, session_key, host, port):
        """ Setting up connection details """
        self._host = host
        self._port = port
        self._session_key = session_key
        
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._ssl_socket = ssl.wrap_socket(self._socket)
        self._ssl_socket.connect((host, port))

    def _send_cmd(self, command):
        """ Generic function to send commands """
        response = self._ssl_socket.write(jdumps(command) + '\n')
        return response

    def login(self):
        """ Logging in to the server """
        cmd = {
            "cmd" : "login", 
            "args" : { 
                "session_key" : self._session_key, 
                "service": "NEXTAPI"
                }
            }
        num_bytes = self._send_cmd(cmd)

    def subscribe(self, market, instrument):
        """ Subscribing to a particular instrument on a market """
        cmd = {
            "cmd" : "subscribe", 
            "args": { 
                "t" : "price", 
                "m" : market, 
                "i" : instrument
                }
            }
        num_bytes = self._send_cmd(cmd)

    def run(self):
        """ Consuming the socket """
        while True:
            message = self._ssl_socket.read()
            if message:
                print message
