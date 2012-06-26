#!/usr/bin/env python

""" 
Module containing all utils
"""

import json

def print_json(j,prefix=''):
    for key, value in j.items():
        if isinstance (value,dict):
            print '%s%s' % (prefix,key)
            print_json(value, prefix+'  ')
        else:
            print '%s%s:%s' % (prefix,key,value)
