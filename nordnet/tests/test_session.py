#!/usr/bin/env python

""" 
Unit tests for all session-related stuff

"""

import pprint
import socket
import ssl
import json

from nordnet.restsession import *

def test_make_hash():
    """ Testing to make a hash-key """
    hashkey = make_hash()
    print hashkey

def test_connect():
    """ Connecting to the HTTP server """
    connection = connect()

def test_get_status():
    """ Connecting and getting the status """
    connection = connect()
    status = get_status(connection)
    print '\nStatus from server:\n' 
    pprint.pprint(status)

def test_login():
    """ Loggon to the HTTP server """
    hashkey = make_hash()
    connection = connect()
    response = login(connection, hashkey)
    print '\nResult from logon:\n'
    pprint.pprint(response)
    print '\nLocal session key: %s' % response['session_key']

def test_public_feed():
    """ Testing the public feed """

    hashkey = make_hash()
    connection = connect()
    
    response = login(connection, hashkey)
    
    session_key = response['session_key']
    hostname = response['public_feed']['hostname']
    port = response['public_feed']['port']
    
    print 'Using host: %s:%s.' % (hostname, port)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = ssl.wrap_socket(s)
    ssl_socket.connect((hostname, port))
    
    #print repr(ssl_sock.getpeername())
    #print ssl_sock.cipher()
    
    cmd = {
        "cmd" : "login", 
        "args" : { 
            "session_key" : session_key, 
            "service": "NEXTAPI"
            }
        }
    
    num_bytes = ssl_socket.write(json.dumps(cmd) + "\n")
    print "Session key sent (%d bytes)" % num_bytes

    market = 11
    instrument = "101" 
    cmd = {
        "cmd" : "subscribe", 
        "args": { 
            "t" : "price", 
            "m" : market, 
            "i" : instrument
            }
        }
    
    num_bytes = ssl_socket.send(json.dumps(cmd) + "\n")
    print "Subscription request sent for market = %d and  instrument = %s (%d bytes)" % (market, instrument, num_bytes)
    
    print "Reading stream"
    while True:
        output = ssl_socket.read()
        print output
    print "Closing socket connection..." 
    del ssl_socket
    s.close()
